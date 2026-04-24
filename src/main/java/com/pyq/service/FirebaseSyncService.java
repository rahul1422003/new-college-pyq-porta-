package com.pyq.service;

import com.google.auth.oauth2.GoogleCredentials;
import com.google.cloud.firestore.Firestore;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.cloud.FirestoreClient;
import com.pyq.model.Feedback;
import com.pyq.model.PlacementQuestion;
import com.pyq.model.PlacementResult;
import com.pyq.model.UserLoginRecord;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.ByteArrayInputStream;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;

@Service
public class FirebaseSyncService {

    @Value("${firebase.enabled:false}")
    private boolean firebaseEnabled;

    @Value("${firebase.project-id:}")
    private String projectId;

    @Value("${firebase.service-account-json:}")
    private String serviceAccountJson;

    private Firestore firestore;
    private boolean initializationAttempted;

    public void syncLoginRecord(UserLoginRecord record) {
        Firestore db = getFirestore();
        if (db == null) return;

        Map<String, Object> data = new LinkedHashMap<>();
        data.put("name", record.getName());
        data.put("enrollment", record.getEnrollment());
        data.put("semester", record.getSemester());
        data.put("loginTime", String.valueOf(record.getLoginTime()));
        db.collection("userLogins").document(String.valueOf(record.getId())).set(data);
    }

    public void syncFeedback(Feedback feedback) {
        Firestore db = getFirestore();
        if (db == null) return;

        Map<String, Object> data = new LinkedHashMap<>();
        data.put("name", feedback.getName());
        data.put("enrollment", feedback.getEnrollment());
        data.put("subject", feedback.getSubject());
        data.put("rating", feedback.getRating());
        data.put("comment", feedback.getComment());
        db.collection("feedback").document(String.valueOf(feedback.getId())).set(data);
    }

    public void syncPlacementQuestion(PlacementQuestion question) {
        Firestore db = getFirestore();
        if (db == null) return;

        Map<String, Object> data = new LinkedHashMap<>();
        data.put("category", question.getCategory());
        data.put("question", question.getQuestion());
        data.put("optionA", question.getOptionA());
        data.put("optionB", question.getOptionB());
        data.put("optionC", question.getOptionC());
        data.put("optionD", question.getOptionD());
        data.put("correctOption", question.getCorrectOption());
        data.put("difficulty", question.getDifficulty());
        data.put("explanation", question.getExplanation());
        db.collection("placementQuestions").document(String.valueOf(question.getId())).set(data);
    }

    public void syncPlacementResult(PlacementResult result) {
        Firestore db = getFirestore();
        if (db == null) return;

        Map<String, Object> data = new LinkedHashMap<>();
        data.put("name", result.getName());
        data.put("enrollment", result.getEnrollment());
        data.put("totalQuestions", result.getTotalQuestions());
        data.put("correctAnswers", result.getCorrectAnswers());
        data.put("scorePercent", result.getScorePercent());
        data.put("attemptedAt", String.valueOf(result.getAttemptedAt()));
        db.collection("placementResults").document(String.valueOf(result.getId())).set(data);
    }

    private synchronized Firestore getFirestore() {
        if (firestore != null) return firestore;
        if (initializationAttempted) return null;
        initializationAttempted = true;

        if (!firebaseEnabled || projectId.isBlank() || serviceAccountJson.isBlank()) {
            return null;
        }

        try {
            if (FirebaseApp.getApps().isEmpty()) {
                GoogleCredentials credentials = GoogleCredentials.fromStream(
                        new ByteArrayInputStream(serviceAccountJson.getBytes(StandardCharsets.UTF_8))
                );

                FirebaseOptions options = FirebaseOptions.builder()
                        .setCredentials(credentials)
                        .setProjectId(projectId)
                        .build();

                FirebaseApp.initializeApp(options);
            }

            firestore = FirestoreClient.getFirestore();
            return firestore;
        } catch (Exception exception) {
            return null;
        }
    }
}
