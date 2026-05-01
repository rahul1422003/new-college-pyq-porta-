package com.pyq.controller;

import com.pyq.model.Feedback;
import com.pyq.repository.FeedbackRepository;
import com.pyq.service.FirebaseSyncService;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
public class FeedbackController {

    @Autowired
    private FeedbackRepository feedbackRepo;

    @Autowired
    private FirebaseSyncService firebaseSyncService;

    @GetMapping("/feedback")
    public String feedbackPage(@RequestParam(required = false) String subject,
                               Model model,
                               HttpSession session) {
        if (!checkUser(session)) return "redirect:/login";

        model.addAttribute("name", session.getAttribute("name"));
        model.addAttribute("enrollment", session.getAttribute("enrollment"));
        model.addAttribute("subject", normalizeSubject(subject));

        return "feedback";
    }

    @PostMapping("/feedback")
    public String saveFeedback(@RequestParam(required = false) String subject,
                               @RequestParam int rating,
                               @RequestParam String comment,
                               HttpSession session,
                               RedirectAttributes redirectAttributes) {
        if (!checkUser(session)) return "redirect:/login";

        String name = (String) session.getAttribute("name");
        String enrollment = (String) session.getAttribute("enrollment");

        Feedback feedback = new Feedback();
        feedback.setName(name);
        feedback.setEnrollment(enrollment);
        feedback.setSubject(normalizeSubject(subject));
        feedback.setRating(rating);
        feedback.setComment(comment);

        feedbackRepo.save(feedback);
        firebaseSyncService.syncFeedback(feedback);

        redirectAttributes.addFlashAttribute("success", "Feedback submitted successfully.");
        return "redirect:/course";
    }

    private boolean checkUser(HttpSession session) {
        return session.getAttribute("role") != null &&
                session.getAttribute("role").equals("USER") &&
                session.getAttribute("enrollment") != null;
    }

    private String normalizeSubject(String subject) {
        if (subject == null || subject.isBlank()) {
            return "General Feedback";
        }

        return subject.trim();
    }
}
