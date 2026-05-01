package com.pyq.repository;

import com.google.cloud.firestore.DocumentSnapshot;
import com.pyq.model.PlacementQuestion;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Repository;

import java.util.Comparator;
import java.util.List;

@Repository
public class FirebasePlacementQuestionRepository extends FirestoreRepositorySupport<PlacementQuestion> implements PlacementQuestionRepository {

    private static final String COLLECTION = "placementQuestions";

    @Override
    public long count() {
        return count(COLLECTION);
    }

    @Override
    public PlacementQuestion save(PlacementQuestion question) {
        if (question.getId() == 0) {
            question.setId(nextId(COLLECTION, PlacementQuestion::getId));
        }
        memory.put(question.getId(), question);
        firebaseSyncService.syncPlacementQuestion(question);
        return question;
    }

    @Override
    public List<PlacementQuestion> findAll(Sort sort) {
        return sorted(findAll(COLLECTION, this::fromDocument), PlacementQuestion::getId, true);
    }

    @Override
    public List<PlacementQuestion> findAllByOrderByCategoryAscDifficultyAscIdDesc() {
        return findAll(COLLECTION, this::fromDocument).stream()
                .sorted(Comparator
                        .comparing(PlacementQuestion::getCategory, Comparator.nullsLast(String::compareToIgnoreCase))
                        .thenComparing(PlacementQuestion::getDifficulty, Comparator.nullsLast(String::compareToIgnoreCase))
                        .thenComparing(Comparator.comparingInt(PlacementQuestion::getId).reversed()))
                .toList();
    }

    @Override
    public void deleteById(int id) {
        delete(COLLECTION, id);
    }

    private PlacementQuestion fromDocument(DocumentSnapshot document) {
        PlacementQuestion question = new PlacementQuestion();
        question.setId(documentId(document));
        question.setCategory(string(document, "category"));
        question.setQuestion(string(document, "question"));
        question.setOptionA(string(document, "optionA"));
        question.setOptionB(string(document, "optionB"));
        question.setOptionC(string(document, "optionC"));
        question.setOptionD(string(document, "optionD"));
        question.setCorrectOption(string(document, "correctOption"));
        question.setDifficulty(string(document, "difficulty"));
        question.setExplanation(string(document, "explanation"));
        return question;
    }
}
