package com.pyq.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.pyq.model.User;
import com.pyq.repository.UserRepository;

@Service
public class UserService {

    @Autowired
    private UserRepository repo;

    // 🔹 Login Method
    public User login(String enrollment, String password) {

        User user = repo.findByEnrollment(enrollment);

        // ✅ Check user exists
        if (user == null) {
            return null;
        }

        // ✅ Check password match
        if (!user.getPassword().equals(password)) {
            return null;
        }

        return user;
    }

    // 🔹 Register Method
    public User register(User user) {

        // ✅ Check duplicate user
        User existingUser = repo.findByEnrollment(user.getEnrollment());

        if (existingUser != null) {
            throw new RuntimeException("User already exists");
        }

         return repo.save(user);
    }

    // 🔹 Find user by enrollment (important for controller)
    public User findByEnrollment(String enrollment) {
        return repo.findByEnrollment(enrollment);
    }
}