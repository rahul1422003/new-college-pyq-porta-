package com.pyq.controller;

import com.pyq.model.UserLoginRecord;
import com.pyq.repository.UserLoginRecordRepository;
import com.pyq.service.FirebaseSyncService;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.time.LocalDateTime;
import java.util.regex.Pattern;

@Controller
public class LoginController {

    private static final Pattern ENROLLMENT_PATTERN = Pattern.compile("^L[A-Za-z]{6}[0-9]{5}$");

    @Autowired
    private UserLoginRecordRepository loginRecordRepo;

    @Autowired
    private FirebaseSyncService firebaseSyncService;

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

        session.setAttribute("name", cleanName);
        session.setAttribute("enrollment", cleanEnrollment);
        session.setAttribute("semester", semester);
        session.setAttribute("role", "USER");

        UserLoginRecord record = new UserLoginRecord();
        record.setName(cleanName);
        record.setEnrollment(cleanEnrollment);
        record.setSemester(semester);
        record.setLoginTime(LocalDateTime.now());
        loginRecordRepo.save(record);
        firebaseSyncService.syncLoginRecord(record);

        redirectAttributes.addFlashAttribute("success", "Login successful. Welcome to LNCT PYQ Portal.");
        return "redirect:/course";
    }

    @GetMapping("/logout")
    public String logout(HttpSession session) {
        session.invalidate();
        return "redirect:/login";
    }
}
