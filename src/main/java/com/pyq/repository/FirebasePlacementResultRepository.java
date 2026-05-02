package com.pyq.repository;

import com.google.cloud.firestore.DocumentSnapshot;
import com.pyq.model.PlacementResult;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class FirebasePlacementResultRepository extends FirestoreRepositorySupport<PlacementResult> implements PlacementResultRepository {

    private static final String COLLECTION = "placementResults";

    @Override
    public long count() {
        return count(COLLECTION);
    }

    @Override
    public PlacementResult save(PlacementResult result) {
        if (result.getId() == 0) {
            result.setId(nextId(COLLECTION, PlacementResult::getId));
        }
        memory.put(result.getId(), result);
        firebaseSyncService.syncPlacementResult(result);
        return result;
    }

    @Override
    public List<PlacementResult> findAll(Sort sort) {
        return sorted(findAll(COLLECTION, this::fromDocument), PlacementResult::getAttemptedAt, true);
    }

    @Override
    public List<PlacementResult> findByEnrollmentOrderByAttemptedAtDesc(String enrollment) {
        return sorted(findAll(COLLECTION, this::fromDocument).stream()
                .filter(result -> enrollment != null && enrollment.equalsIgnoreCase(result.getEnrollment()))
                .toList(), PlacementResult::getAttemptedAt, true);
    }

    @Override
    public List<PlacementResult> findByEnrollmentAndCategoryOrderByAttemptedAtDesc(String enrollment, String category) {
        return sorted(findAll(COLLECTION, this::fromDocument).stream()
                .filter(result -> enrollment != null && enrollment.equalsIgnoreCase(result.getEnrollment()))
                .filter(result -> category != null && category.equalsIgnoreCase(result.getCategory()))
                .toList(), PlacementResult::getAttemptedAt, true);
    }

    @Override
    public void deleteById(int id) {
        delete(COLLECTION, id);
    }

    private PlacementResult fromDocument(DocumentSnapshot document) {
        PlacementResult result = new PlacementResult();
        result.setId(documentId(document));
        result.setName(string(document, "name"));
        result.setEnrollment(string(document, "enrollment"));
        result.setCategory(string(document, "category"));
        result.setTotalQuestions(integer(document, "totalQuestions"));
        result.setCorrectAnswers(integer(document, "correctAnswers"));
        result.setScorePercent(integer(document, "scorePercent"));
        result.setAttemptedAt(dateTime(document, "attemptedAt"));
        return result;
    }
}
