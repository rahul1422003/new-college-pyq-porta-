package com.pyq.repository;

import com.pyq.model.PlacementQuestion;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface PlacementQuestionRepository extends JpaRepository<PlacementQuestion, Integer> {

    List<PlacementQuestion> findAllByOrderByCategoryAscDifficultyAscIdDesc();

    default List<PlacementQuestion> latestFirst() {
        return findAll(Sort.by(Sort.Direction.DESC, "id"));
    }
}
