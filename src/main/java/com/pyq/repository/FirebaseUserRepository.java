package com.pyq.repository;

import com.google.cloud.firestore.DocumentSnapshot;
import com.pyq.model.User;
import com.pyq.util.AppClock;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;

@Repository
public class FirebaseUserRepository extends FirestoreRepositorySupport<User> implements UserRepository {

    private static final String COLLECTION = "users";

    @Override
    public long count() {
        return count(COLLECTION);
    }

    @Override
    public List<User> findAll(Sort sort) {
        return sorted(findAll(COLLECTION, this::fromDocument), User::getId, true);
    }

    @Override
    public User save(User user) {
        LocalDateTime now = AppClock.now();
        if (user.getId() == 0) {
            user.setId(nextId(COLLECTION, User::getId));
            user.setCreatedAt(now);
        }
        user.setUpdatedAt(now);
        if (user.getRole() == null || user.getRole().isBlank()) {
            user.setRole("USER");
        }

        memory.put(user.getId(), user);
        firebaseSyncService.syncUser(user);
        return user;
    }

    @Override
    public User findByEnrollment(String enrollment) {
        if (enrollment == null) return null;
        return findAll(COLLECTION, this::fromDocument).stream()
                .filter(user -> enrollment.equalsIgnoreCase(user.getEnrollment()))
                .findFirst()
                .orElse(null);
    }

    @Override
    public User findByEmail(String email) {
        if (email == null) return null;
        return findAll(COLLECTION, this::fromDocument).stream()
                .filter(user -> email.equalsIgnoreCase(user.getEmail()))
                .findFirst()
                .orElse(null);
    }

    @Override
    public void deleteById(int id) {
        delete(COLLECTION, id);
    }

    private User fromDocument(DocumentSnapshot document) {
        User user = new User();
        user.setId(documentId(document));
        user.setName(string(document, "name"));
        user.setEnrollment(string(document, "enrollment"));
        user.setSemester(string(document, "semester"));
        user.setCourse(string(document, "course"));
        user.setPhone(string(document, "phone"));
        user.setEmail(string(document, "email"));
        user.setProfileImagePath(string(document, "profileImagePath"));
        user.setPassword(string(document, "password"));
        user.setRole(string(document, "role"));
        user.setCreatedAt(dateTime(document, "createdAt"));
        user.setUpdatedAt(dateTime(document, "updatedAt"));
        user.setLastLoginAt(dateTime(document, "lastLoginAt"));
        return user;
    }
}
