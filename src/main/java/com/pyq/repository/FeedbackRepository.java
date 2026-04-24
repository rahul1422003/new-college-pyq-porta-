package com.pyq.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.pyq.model.Feedback;

public interface FeedbackRepository extends JpaRepository<Feedback, Integer> {
}