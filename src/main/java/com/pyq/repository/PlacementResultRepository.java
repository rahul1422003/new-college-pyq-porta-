package com.pyq.repository;

import com.pyq.model.PlacementResult;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface PlacementResultRepository extends JpaRepository<PlacementResult, Integer> {

    List<PlacementResult> findByEnrollmentOrderByAttemptedAtDesc(String enrollment);

    default List<PlacementResult> latestFirst() {
        return findAll(Sort.by(Sort.Direction.DESC, "attemptedAt"));
    }
}
