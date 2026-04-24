package com.pyq.controller;

import com.pyq.model.PlacementQuestion;
import com.pyq.repository.FeedbackRepository;
import com.pyq.repository.PlacementQuestionRepository;
import com.pyq.repository.PlacementResultRepository;
import com.pyq.repository.UserLoginRecordRepository;
import com.pyq.repository.UserRepository;
import com.pyq.service.FileStorageService;
import com.pyq.service.FirebaseSyncService;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("/admin")
public class Admincontroller {

    @Autowired
    private FeedbackRepository feedbackRepo;

    @Autowired
    private UserRepository userRepo;

    @Autowired
    private PlacementQuestionRepository questionRepo;

    @Autowired
    private PlacementResultRepository resultRepo;

    @Autowired
    private UserLoginRecordRepository loginRecordRepo;

    @Autowired
    private FileStorageService fileStorageService;

    @Autowired
    private FirebaseSyncService firebaseSyncService;

    @Value("${app.admin.email:admin@gmail.com}")
    private String adminEmail;

    @Value("${app.admin.password:admin123}")
    private String adminPassword;

    private boolean checkAdmin(HttpSession session) {
        return session.getAttribute("role") != null &&
                session.getAttribute("role").equals("ADMIN");
    }

    @GetMapping("/login")
    public String adminLoginPage() {
        return "admin";
    }

    @PostMapping("/login")
    public String adminLogin(@RequestParam String email,
                             @RequestParam String password,
                             HttpSession session,
                             RedirectAttributes redirectAttributes) {

        if (email.equals(adminEmail) && password.equals(adminPassword)) {
            session.setAttribute("name", "Admin");
            session.setAttribute("role", "ADMIN");
            redirectAttributes.addFlashAttribute("success", "Welcome back, Admin.");
            return "redirect:/admin/dashboard";
        }

        redirectAttributes.addFlashAttribute("error", "Invalid admin email or password.");
        return "redirect:/admin/login";
    }

    @GetMapping("/dashboard")
    public String adminDashboard(HttpSession session, Model model) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        model.addAttribute("totalUsers", userRepo.count());
        model.addAttribute("totalFeedback", feedbackRepo.count());
        model.addAttribute("totalQuestions", questionRepo.count());
        model.addAttribute("totalResults", resultRepo.count());
        model.addAttribute("totalLogins", loginRecordRepo.count());
        model.addAttribute("recentResults", resultRepo.latestFirst().stream().limit(5).toList());
        model.addAttribute("recentLogins", loginRecordRepo.latestFirst().stream().limit(5).toList());
        return "admin-dashboard";
    }

    @GetMapping("/upload")
    public String uploadPage(HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        return "admin-upload";
    }

    @PostMapping("/upload")
    public String uploadFile(@RequestParam("subject") String subject,
                             @RequestParam("file") MultipartFile file,
                             HttpSession session,
                             RedirectAttributes redirectAttributes) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        try {
            String storedFile = fileStorageService.storePdf(file, subject);
            redirectAttributes.addFlashAttribute("success",
                    "PDF uploaded successfully as " + storedFile);
        } catch (IllegalArgumentException e) {
            redirectAttributes.addFlashAttribute("error", e.getMessage());
            return "redirect:/admin/upload";
        } catch (Exception e) {
            redirectAttributes.addFlashAttribute("error",
                    "Upload failed. Please try again.");
            return "redirect:/admin/upload";
        }

        return "redirect:/admin/upload";
    }

    @GetMapping("/feedback")
    public String viewFeedback(Model model, HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        model.addAttribute("list",
                feedbackRepo.findAll(Sort.by(Sort.Direction.DESC, "id"))
        );

        return "view-feedback";
    }

    @GetMapping("/delete-feedback/{id}")
    public String deleteFeedback(@PathVariable int id, HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        feedbackRepo.deleteById(id);
        return "redirect:/admin/feedback";
    }

    @GetMapping("/placement-quiz")
    public String placementQuiz(Model model, HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        model.addAttribute("questions", questionRepo.latestFirst());
        model.addAttribute("newQuestion", new PlacementQuestion());
        return "admin-placement-quiz";
    }

    @PostMapping("/placement-quiz")
    public String savePlacementQuestion(@ModelAttribute PlacementQuestion question,
                                        HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        questionRepo.save(question);
        firebaseSyncService.syncPlacementQuestion(question);
        return "redirect:/admin/placement-quiz";
    }

    @GetMapping("/delete-question/{id}")
    public String deletePlacementQuestion(@PathVariable int id, HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        questionRepo.deleteById(id);
        return "redirect:/admin/placement-quiz";
    }

    @GetMapping("/placement-results")
    public String placementResults(Model model, HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        model.addAttribute("results", resultRepo.latestFirst());
        return "admin-placement-results";
    }

    @GetMapping("/delete-result/{id}")
    public String deletePlacementResult(@PathVariable int id, HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        resultRepo.deleteById(id);
        return "redirect:/admin/placement-results";
    }

    @GetMapping("/manage-users")
    public String manageUsers(Model model, HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        model.addAttribute("users", userRepo.findAll(Sort.by(Sort.Direction.DESC, "id")));
        return "admin-manage-users";
    }

    @GetMapping("/delete-user/{id}")
    public String deleteUser(@PathVariable int id, HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        userRepo.deleteById(id);
        return "redirect:/admin/manage-users";
    }

    @GetMapping("/user-logins")
    public String userLogins(Model model, HttpSession session) {
        if (!checkAdmin(session)) return "redirect:/admin/login";

        model.addAttribute("logins", loginRecordRepo.latestFirst());
        return "admin-user-logins";
    }

    @GetMapping("/logout")
    public String logout(HttpSession session) {
        session.invalidate();
        return "redirect:/admin/login";
    }
}
