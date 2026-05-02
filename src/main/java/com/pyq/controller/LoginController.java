package com.pyq.controller;

import com.pyq.model.UserLoginRecord;
import com.pyq.repository.UserLoginRecordRepository;
import com.pyq.service.FirebaseSyncService;
import com.pyq.service.UserService;
import com.pyq.util.AppClock;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.util.regex.Pattern;

@Controller
public class LoginController {

    private static final Pattern ENROLLMENT_PATTERN = Pattern.compile("^L[A-Za-z]{6}[0-9]{5}$");

    @Autowired
    private UserLoginRecordRepository loginRecordRepo;

    @Autowired
    private FirebaseSyncService firebaseSyncService;

    @Autowired
    private UserService userService;

    @GetMapping("/login")
    public String loginPage() {
        return "login";
    }

    @PostMapping("/login")
    public String userLogin(@RequestParam String name,
                            @RequestParam String enrollment,
                            @RequestParam String semester,
                            HttpSession session,
                            RedirectAttributes redirectAttributes) {

        if (name == null || name.isEmpty() ||
                enrollment == null || enrollment.isEmpty() ||
                semester == null || semester.isEmpty()) {
            redirectAttributes.addFlashAttribute("error", "Please fill all login details.");
            return "redirect:/login";
        }

        String cleanName = name.trim().replaceAll("\\s+", " ");
        String cleanEnrollment = enrollment.trim().toUpperCase();
        if (cleanName.length() < 3) {
            redirectAttributes.addFlashAttribute("error", "Name must be at least 3 characters.");
            return "redirect:/login";
        }

        if (!ENROLLMENT_PATTERN.matcher(cleanEnrollment).matches()) {
            redirectAttributes.addFlashAttribute("error", "Invalid enrollment number format.");
            return "redirect:/login";
        }

        var user = userService.createOrUpdateStudent(cleanName, cleanEnrollment, semester);

        session.setAttribute("userId", user.getId());
        session.setAttribute("name", user.getName());
        session.setAttribute("enrollment", user.getEnrollment());
        session.setAttribute("semester", user.getSemester());
        session.setAttribute("role", "USER");

        UserLoginRecord record = new UserLoginRecord();
        record.setName(user.getName());
        record.setEnrollment(user.getEnrollment());
        record.setSemester(user.getSemester());
        record.setLoginTime(AppClock.now());
        loginRecordRepo.save(record);
        firebaseSyncService.syncLoginRecord(record);

        redirectAttributes.addFlashAttribute("success", "Login successful. Your dashboard is ready.");
        return "redirect:/dashboard";
    }

    @GetMapping("/logout")
    public String logout(HttpSession session) {
        session.invalidate();
        return "redirect:/login";
    }
}
