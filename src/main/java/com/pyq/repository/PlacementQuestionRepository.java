package com.pyq.repository;

import com.pyq.model.PlacementQuestion;
import org.springframework.data.domain.Sort;

import java.util.List;

public interface PlacementQuestionRepository {

    long count();

    PlacementQuestion save(PlacementQuestion question);

    List<PlacementQuestion> findAll(Sort sort);

    List<PlacementQuestion> findAllByOrderByCategoryAscDifficultyAscIdDesc();

    default List<PlacementQuestion> latestFirst() {
        return findAll(Sort.by(Sort.Direction.DESC, "id"));
    }

    void deleteById(int id);
}
