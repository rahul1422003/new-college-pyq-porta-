package com.pyq.repository;

import com.pyq.model.UserLoginRecord;
import org.springframework.data.domain.Sort;

import java.util.List;

public interface UserLoginRecordRepository {

    long count();

    UserLoginRecord save(UserLoginRecord record);

    List<UserLoginRecord> findAll(Sort sort);

    default List<UserLoginRecord> latestFirst() {
        return findAll(Sort.by(Sort.Direction.DESC, "loginTime"));
    }
}
