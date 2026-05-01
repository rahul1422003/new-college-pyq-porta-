package com.pyq.repository;

import com.google.cloud.firestore.DocumentSnapshot;
import com.google.cloud.firestore.Firestore;
import com.pyq.service.FirebaseSyncService;
import org.springframework.beans.factory.annotation.Autowired;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.Function;
import java.util.function.ToIntFunction;

abstract class FirestoreRepositorySupport<T> {

    @Autowired
    protected FirebaseSyncService firebaseSyncService;

    protected final Map<Integer, T> memory = new ConcurrentHashMap<>();

    protected Firestore firestore() {
        return firebaseSyncService.getFirestore();
    }

    protected List<T> findAll(String collection, Function<DocumentSnapshot, T> mapper) {
        Firestore db = firestore();
        if (db == null) {
            return new ArrayList<>(memory.values());
        }

        try {
            return db.collection(collection).get().get().getDocuments().stream()
                    .map(mapper)
                    .toList();
        } catch (Exception exception) {
            return new ArrayList<>(memory.values());
        }
    }

    protected long count(String collection) {
        Firestore db = firestore();
        if (db == null) {
            return memory.size();
        }

        try {
            return db.collection(collection).get().get().size();
        } catch (Exception exception) {
            return memory.size();
        }
    }

    protected void delete(String collection, int id) {
        memory.remove(id);
        Firestore db = firestore();
        if (db == null) return;

        try {
            db.collection(collection).document(String.valueOf(id)).delete().get();
        } catch (Exception ignored) {
        }
    }

    protected int nextId(String collection, ToIntFunction<T> idReader) {
        int maxId = memory.values().stream().mapToInt(idReader).max().orElse(0);
        Firestore db = firestore();
        if (db == null) {
            return maxId + 1;
        }

        try {
            for (DocumentSnapshot document : db.collection(collection).get().get().getDocuments()) {
                try {
                    maxId = Math.max(maxId, Integer.parseInt(document.getId()));
                } catch (NumberFormatException ignored) {
                }
            }
        } catch (Exception ignored) {
        }

        return maxId + 1;
    }

    protected String string(DocumentSnapshot document, String field) {
        return document.getString(field);
    }

    protected int integer(DocumentSnapshot document, String field) {
        Long value = document.getLong(field);
        return value == null ? 0 : value.intValue();
    }

    protected LocalDateTime dateTime(DocumentSnapshot document, String field) {
        String value = document.getString(field);
        if (value == null || value.isBlank() || "null".equals(value)) {
            return null;
        }

        try {
            return LocalDateTime.parse(value);
        } catch (Exception exception) {
            return null;
        }
    }

    protected int documentId(DocumentSnapshot document) {
        try {
            return Integer.parseInt(document.getId());
        } catch (NumberFormatException exception) {
            return 0;
        }
    }

    protected <V extends Comparable<? super V>> List<T> sorted(List<T> values,
                                                               Function<T, V> key,
                                                               boolean descending) {
        Comparator<T> comparator = Comparator.comparing(
                key,
                Comparator.nullsLast(Comparator.naturalOrder())
        );
        if (descending) {
            comparator = comparator.reversed();
        }
        return values.stream().sorted(comparator).toList();
    }
}
