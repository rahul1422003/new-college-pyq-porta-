package com.pyq.repository;

import com.pyq.model.PlacementResult;
import org.springframework.data.domain.Sort;

import java.util.List;

public interface PlacementResultRepository {

    long count();

    PlacementResult save(PlacementResult result);

    List<PlacementResult> findAll(Sort sort);

    List<PlacementResult> findByEnrollmentOrderByAttemptedAtDesc(String enrollment);

    default List<PlacementResult> latestFirst() {
        return findAll(Sort.by(Sort.Direction.DESC, "attemptedAt"));
    }

    void deleteById(int id);
}
