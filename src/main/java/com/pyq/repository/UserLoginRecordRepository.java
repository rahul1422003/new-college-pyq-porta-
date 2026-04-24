package com.pyq.repository;

import com.pyq.model.UserLoginRecord;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface UserLoginRecordRepository extends JpaRepository<UserLoginRecord, Integer> {

    default List<UserLoginRecord> latestFirst() {
        return findAll(Sort.by(Sort.Direction.DESC, "loginTime"));
    }
}
