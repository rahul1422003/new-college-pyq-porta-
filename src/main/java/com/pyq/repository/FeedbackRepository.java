package com.pyq.repository;

import com.pyq.model.Feedback;
import org.springframework.data.domain.Sort;

import java.util.List;

public interface FeedbackRepository {

    long count();

    List<Feedback> findAll(Sort sort);

    Feedback save(Feedback feedback);

    void deleteById(int id);
}
