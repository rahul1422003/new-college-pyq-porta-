package com.pyq.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.pyq.model.User;

public interface UserRepository extends JpaRepository<User, Integer> {

    User findByEnrollment(String enrollment);

    User findByEmail(String email);  // 🔥 important
}