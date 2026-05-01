package com.pyq.repository;

import com.google.cloud.firestore.DocumentSnapshot;
import com.pyq.model.Feedback;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class FirebaseFeedbackRepository extends FirestoreRepositorySupport<Feedback> implements FeedbackRepository {

    private static final String COLLECTION = "feedback";

    @Override
    public long count() {
        return count(COLLECTION);
    }

    @Override
    public List<Feedback> findAll(Sort sort) {
        return sorted(findAll(COLLECTION, this::fromDocument), Feedback::getId, true);
    }

    @Override
    public Feedback save(Feedback feedback) {
        if (feedback.getId() == 0) {
            feedback.setId(nextId(COLLECTION, Feedback::getId));
        }
        memory.put(feedback.getId(), feedback);
        firebaseSyncService.syncFeedback(feedback);
        return feedback;
    }

    @Override
    public void deleteById(int id) {
        delete(COLLECTION, id);
    }

    private Feedback fromDocument(DocumentSnapshot document) {
        Feedback feedback = new Feedback();
        feedback.setId(documentId(document));
        feedback.setName(string(document, "name"));
        feedback.setEnrollment(string(document, "enrollment"));
        feedback.setSubject(string(document, "subject"));
        feedback.setRating(integer(document, "rating"));
        feedback.setComment(string(document, "comment"));
        return feedback;
    }
}
