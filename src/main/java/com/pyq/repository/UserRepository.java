package com.pyq.repository;

import com.pyq.model.User;
import org.springframework.data.domain.Sort;

import java.util.List;

public interface UserRepository {

    long count();

    List<User> findAll(Sort sort);

    User save(User user);

    User findByEnrollment(String enrollment);

    User findByEmail(String email);

    void deleteById(int id);
}
