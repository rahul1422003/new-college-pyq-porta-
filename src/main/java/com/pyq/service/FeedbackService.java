package com.pyq.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.pyq.model.Feedback;
import com.pyq.repository.FeedbackRepository;

@Service
public class FeedbackService {

    @Autowired
    private FeedbackRepository repo;

    public void saveFeedback(Feedback f){
        repo.save(f);
    }
}