package com.pyq.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.pyq.model.User;
import com.pyq.repository.UserRepository;
import com.pyq.util.AppClock;

@Service
public class UserService {

    @Autowired
    private UserRepository repo;

    public User login(String enrollment, String password) {
        User user = repo.findByEnrollment(enrollment);

        if (user == null) {
            return null;
        }

        if (!user.getPassword().equals(password)) {
            return null;
        }

        return user;
    }

    public User register(User user) {
        User existingUser = repo.findByEnrollment(user.getEnrollment());

        if (existingUser != null) {
            throw new RuntimeException("User already exists");
        }

        user.setEnrollment(normalizeEnrollment(user.getEnrollment()));
        user.setName(normalizeName(user.getName()));
        user.setSemester(normalizeRequired(user.getSemester()));
        user.setEmail(normalizeOptional(user.getEmail()));
        user.setCourse(normalizeOptional(user.getCourse()));
        user.setPhone(normalizeOptional(user.getPhone()));
        user.setRole(defaultRole(user.getRole()));
        user.setLastLoginAt(AppClock.now());
        return repo.save(user);
    }

    public User findByEnrollment(String enrollment) {
        return repo.findByEnrollment(enrollment);
    }

    public User createOrUpdateStudent(String name, String enrollment, String semester) {
        String cleanEnrollment = normalizeEnrollment(enrollment);
        User user = repo.findByEnrollment(cleanEnrollment);

        if (user == null) {
            user = new User();
            user.setEnrollment(cleanEnrollment);
            user.setRole("USER");
        }

        user.setName(normalizeName(name));
        user.setSemester(normalizeRequired(semester));
        user.setLastLoginAt(AppClock.now());

        if (user.getRole() == null || user.getRole().isBlank()) {
            user.setRole("USER");
        }

        return repo.save(user);
    }

    public User updateProfile(String enrollment,
                              String name,
                              String semester,
                              String email,
                              String phone,
                              String course,
                              String profileImagePath) {
        User user = findRequiredByEnrollment(enrollment);
        user.setName(normalizeName(name));
        user.setSemester(normalizeRequired(semester));
        user.setEmail(normalizeOptional(email));
        user.setPhone(normalizeOptional(phone));
        user.setCourse(normalizeOptional(course));
        if (profileImagePath != null && !profileImagePath.isBlank()) {
            user.setProfileImagePath(profileImagePath);
        }
        return repo.save(user);
    }

    public User findRequiredByEnrollment(String enrollment) {
        User user = repo.findByEnrollment(normalizeEnrollment(enrollment));
        if (user == null) {
            throw new RuntimeException("User not found");
        }
        return user;
    }

    private String normalizeName(String value) {
        return normalizeRequired(value).replaceAll("\\s+", " ");
    }

    private String normalizeEnrollment(String value) {
        return normalizeRequired(value).toUpperCase();
    }

    private String normalizeRequired(String value) {
        if (value == null) {
            throw new RuntimeException("Required value is missing");
        }

        String trimmed = value.trim();
        if (trimmed.isEmpty()) {
            throw new RuntimeException("Required value is missing");
        }

        return trimmed;
    }

    private String normalizeOptional(String value) {
        if (value == null) {
            return null;
        }

        String trimmed = value.trim();
        return trimmed.isEmpty() ? null : trimmed;
    }

    private String defaultRole(String role) {
        return (role == null || role.isBlank()) ? "USER" : role;
    }
}
