package com.pyq.controller;

import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import com.pyq.model.PlacementQuestion;
import com.pyq.model.PlacementResult;
import com.pyq.model.User;
import com.pyq.model.UserDownload;
import com.pyq.repository.PlacementQuestionRepository;
import com.pyq.repository.PlacementResultRepository;
import com.pyq.repository.UserDownloadRepository;
import com.pyq.service.FeedbackService;
import com.pyq.service.FirebaseSyncService;
import com.pyq.service.UserService;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;
import org.springframework.http.ContentDisposition;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.charset.StandardCharsets;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.UUID;

@Controller
public class UserController {

    @Autowired
    private FeedbackService feedbackService;

    @Autowired
    private PlacementQuestionRepository questionRepo;

    @Autowired
    private PlacementResultRepository resultRepo;

    @Autowired
    private UserDownloadRepository downloadRepo;

    @Autowired
    private FirebaseSyncService firebaseSyncService;

    @Autowired
    private UserService userService;

    private boolean checkUser(HttpSession session) {
        return session.getAttribute("role") != null &&
                session.getAttribute("role").equals("USER") &&
                session.getAttribute("enrollment") != null;
    }

    private void setUserData(HttpSession session, Model model) {
        User user = getCurrentUser(session);

        if (user != null) {
            syncSession(session, user);
            model.addAttribute("user", user);
            model.addAttribute("name", user.getName());
            model.addAttribute("enrollment", user.getEnrollment());
            model.addAttribute("semester", user.getSemester());
            model.addAttribute("profileCompletion", calculateProfileCompletion(user));
            return;
        }

        model.addAttribute("name", session.getAttribute("name"));
        model.addAttribute("enrollment", session.getAttribute("enrollment"));
        model.addAttribute("semester", session.getAttribute("semester"));
        model.addAttribute("profileCompletion", 50);
    }

    private User getCurrentUser(HttpSession session) {
        Object enrollment = session.getAttribute("enrollment");
        if (!(enrollment instanceof String value) || value.isBlank()) {
            return null;
        }

        return userService.findByEnrollment(value);
    }

    private void syncSession(HttpSession session, User user) {
        session.setAttribute("userId", user.getId());
        session.setAttribute("name", user.getName());
        session.setAttribute("enrollment", user.getEnrollment());
        session.setAttribute("semester", user.getSemester());
        session.setAttribute("role", user.getRole() == null ? "USER" : user.getRole());
    }

    private int calculateProfileCompletion(User user) {
        int completedFields = 0;

        if (hasValue(user.getName())) completedFields++;
        if (hasValue(user.getEnrollment())) completedFields++;
        if (hasValue(user.getSemester())) completedFields++;
        if (hasValue(user.getEmail())) completedFields++;
        if (hasValue(user.getPhone())) completedFields++;
        if (hasValue(user.getCourse())) completedFields++;
        if (hasValue(user.getProfileImagePath())) completedFields++;

        return (int) Math.round((completedFields / 7.0) * 100);
    }

    private boolean hasValue(String value) {
        return value != null && !value.isBlank();
    }

    private String resolveSemesterRoute(String semester) {
        if (semester == null) {
            return "/sem";
        }

        String digits = semester.replaceAll("[^0-9]", "");
        if (digits.isEmpty()) {
            return "/sem";
        }

        return "/sem" + digits;
    }

    @GetMapping("/")
    public String homeRedirect() {
        return "redirect:/login";
    }

    @GetMapping("/dashboard")
    public String dashboard(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";

        User user = getCurrentUser(session);
        if (user == null) {
            session.invalidate();
            return "redirect:/login";
        }

        syncSession(session, user);
        setUserData(session, model);
        var results = resultRepo.findByEnrollmentOrderByAttemptedAtDesc(user.getEnrollment());
        int bestScore = results.stream().mapToInt(PlacementResult::getScorePercent).max().orElse(0);
        int latestScore = results.isEmpty() ? 0 : results.get(0).getScorePercent();
        int averageScore = results.isEmpty() ? 0 :
                (int) Math.round(results.stream().mapToInt(PlacementResult::getScorePercent).average().orElse(0));

        model.addAttribute("recentResults", results.stream().limit(5).toList());
        model.addAttribute("attemptCount", results.size());
        model.addAttribute("bestScore", bestScore);
        model.addAttribute("latestScore", latestScore);
        model.addAttribute("averageScore", averageScore);
        model.addAttribute("questionCount", questionRepo.count());
        model.addAttribute("recentDownloads",
                downloadRepo.findByEnrollmentOrderByDownloadedAtDesc(user.getEnrollment()).stream().limit(6).toList());
        model.addAttribute("downloadCount", downloadRepo.countByEnrollment(user.getEnrollment()));
        model.addAttribute("semesterRoute", resolveSemesterRoute(user.getSemester()));
        return "dashboard";
    }

    @GetMapping("/pdf/{fileName:.+}")
    public String previewPaper(@PathVariable String fileName,
                               HttpSession session,
                               Model model) {
        if (!checkUser(session)) {
            return "redirect:/login";
        }

        if (isUnsafePdfName(fileName) || !pdfExists(fileName)) {
            return "error";
        }

        model.addAttribute("paperName", fileName);
        model.addAttribute("viewUrl", "/pdf/view/" + fileName);
        model.addAttribute("downloadUrl", "/pdf/download/" + fileName);
        return "pdf-preview";
    }

    @GetMapping("/pdf/view/{fileName:.+}")
    public ResponseEntity<Resource> viewPaper(@PathVariable String fileName,
                                              HttpSession session) throws IOException {
        if (!checkUser(session)) {
            return redirectToLogin();
        }

        if (isUnsafePdfName(fileName)) {
            return ResponseEntity.badRequest().build();
        }

        ClassPathResource resource = getPdfResource(fileName);
        if (!resource.exists() || !resource.isReadable()) {
            return ResponseEntity.notFound().build();
        }

        ContentDisposition disposition = ContentDisposition.inline()
                .filename(fileName, StandardCharsets.UTF_8)
                .build();

        return ResponseEntity.ok()
                .contentType(MediaType.APPLICATION_PDF)
                .contentLength(resource.contentLength())
                .header(HttpHeaders.CONTENT_DISPOSITION, disposition.toString())
                .body(resource);
    }

    @GetMapping("/pdf/download/{fileName:.+}")
    public ResponseEntity<Resource> downloadPaper(@PathVariable String fileName,
                                                  HttpSession session) throws IOException {
        if (!checkUser(session)) {
            return redirectToLogin();
        }

        if (isUnsafePdfName(fileName)) {
            return ResponseEntity.badRequest().build();
        }

        ClassPathResource resource = getPdfResource(fileName);
        if (!resource.exists() || !resource.isReadable()) {
            return ResponseEntity.notFound().build();
        }

        saveDownloadRecord(session, fileName);

        ContentDisposition disposition = ContentDisposition.attachment()
                .filename(fileName, StandardCharsets.UTF_8)
                .build();

        return ResponseEntity.ok()
                .contentType(MediaType.APPLICATION_PDF)
                .contentLength(resource.contentLength())
                .header(HttpHeaders.CONTENT_DISPOSITION, disposition.toString())
                .body(resource);
    }

    private ResponseEntity<Resource> redirectToLogin() {
        return ResponseEntity.status(302)
                .header(HttpHeaders.LOCATION, "/login")
                .build();
    }

    private boolean pdfExists(String fileName) {
        ClassPathResource resource = getPdfResource(fileName);
        return resource.exists() && resource.isReadable();
    }

    private ClassPathResource getPdfResource(String fileName) {
        return new ClassPathResource("static/pdf/" + fileName);
    }

    private boolean isUnsafePdfName(String fileName) {
        return fileName == null ||
                fileName.isBlank() ||
                fileName.contains("..") ||
                fileName.contains("/") ||
                fileName.contains("\\") ||
                !fileName.toLowerCase(Locale.ROOT).endsWith(".pdf");
    }

    private void saveDownloadRecord(HttpSession session, String fileName) {
        UserDownload download = new UserDownload();
        download.setName((String) session.getAttribute("name"));
        download.setEnrollment((String) session.getAttribute("enrollment"));
        download.setSemester((String) session.getAttribute("semester"));
        download.setPaperName(fileName);
        download.setPaperPath("/pdf/" + fileName);
        download.setDownloadedAt(LocalDateTime.now());
        downloadRepo.save(download);
    }

    @GetMapping("/course")
    public String course(HttpSession session, Model model) {
        if (session.getAttribute("role") == null ||
                !session.getAttribute("role").equals("USER")) {

            return "redirect:/login";
        }

        setUserData(session, model);
        var results = resultRepo.findByEnrollmentOrderByAttemptedAtDesc((String) session.getAttribute("enrollment"));
        model.addAttribute("recentResults", results.stream().limit(3).toList());
        model.addAttribute("attemptCount", results.size());
        model.addAttribute("bestScore", results.stream().mapToInt(PlacementResult::getScorePercent).max().orElse(0));
        model.addAttribute("latestScore", results.isEmpty() ? 0 : results.get(0).getScorePercent());
        model.addAttribute("questionCount", questionRepo.count());
        model.addAttribute("semesterRoute", resolveSemesterRoute((String) session.getAttribute("semester")));

        return "course";
    }

    @GetMapping("/profile")
    public String profile(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";

        User user = getCurrentUser(session);
        if (user == null) {
            session.invalidate();
            return "redirect:/login";
        }

        syncSession(session, user);
        setUserData(session, model);
        return "profile";
    }

    @PostMapping("/profile/update")
    public String updateProfile(@RequestParam String name,
                                @RequestParam String semester,
                                @RequestParam(required = false) String email,
                                @RequestParam(required = false) String phone,
                                @RequestParam(required = false) String course,
                                @RequestParam(required = false) MultipartFile profileImage,
                                HttpSession session,
                                RedirectAttributes redirectAttributes) {
        if (!checkUser(session)) return "redirect:/login";

        String cleanName = name == null ? "" : name.trim().replaceAll("\\s+", " ");
        String cleanSemester = semester == null ? "" : semester.trim();
        String cleanEmail = email == null ? "" : email.trim();
        String cleanPhone = phone == null ? "" : phone.trim();
        String cleanCourse = course == null ? "" : course.trim();

        if (cleanName.length() < 3) {
            redirectAttributes.addFlashAttribute("error", "Name must be at least 3 characters.");
            return "redirect:/profile";
        }

        if (cleanSemester.isEmpty()) {
            redirectAttributes.addFlashAttribute("error", "Please select your semester.");
            return "redirect:/profile";
        }

        if (!cleanEmail.isEmpty() && !cleanEmail.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$")) {
            redirectAttributes.addFlashAttribute("error", "Please enter a valid email address.");
            return "redirect:/profile";
        }

        if (!cleanPhone.isEmpty() && !cleanPhone.matches("^[0-9]{10}$")) {
            redirectAttributes.addFlashAttribute("error", "Phone number must be 10 digits.");
            return "redirect:/profile";
        }

        String profileImagePath = null;
        if (profileImage != null && !profileImage.isEmpty()) {
            try {
                profileImagePath = saveProfileImage(profileImage);
            } catch (IllegalArgumentException exception) {
                redirectAttributes.addFlashAttribute("error", exception.getMessage());
                return "redirect:/profile";
            } catch (IOException exception) {
                redirectAttributes.addFlashAttribute("error", "Unable to upload profile picture. Please try again.");
                return "redirect:/profile";
            }
        }

        User updatedUser = userService.updateProfile(
                (String) session.getAttribute("enrollment"),
                cleanName,
                cleanSemester,
                cleanEmail,
                cleanPhone,
                cleanCourse,
                profileImagePath
        );

        syncSession(session, updatedUser);
        redirectAttributes.addFlashAttribute("success", "Profile updated successfully.");
        return "redirect:/dashboard";
    }

    private String saveProfileImage(MultipartFile profileImage) throws IOException {
        String contentType = profileImage.getContentType();
        if (contentType == null || !contentType.toLowerCase(Locale.ROOT).startsWith("image/")) {
            throw new IllegalArgumentException("Please upload a valid image file.");
        }

        String originalName = profileImage.getOriginalFilename() == null ? "" : profileImage.getOriginalFilename();
        String extension = getExtension(originalName);
        if (!List.of(".jpg", ".jpeg", ".png", ".webp").contains(extension)) {
            throw new IllegalArgumentException("Profile picture must be JPG, PNG, or WEBP.");
        }

        Path uploadDir = Paths.get(System.getProperty("user.dir"), "uploads", "profile-pics");
        Files.createDirectories(uploadDir);

        String fileName = UUID.randomUUID() + extension;
        Path target = uploadDir.resolve(fileName).normalize();
        profileImage.transferTo(target);
        return "/uploads/profile-pics/" + fileName;
    }

    private String getExtension(String fileName) {
        int dotIndex = fileName.lastIndexOf('.');
        if (dotIndex < 0) {
            return "";
        }

        return fileName.substring(dotIndex).toLowerCase(Locale.ROOT);
    }

    @GetMapping("/sem")
    public String sem(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "sem";
    }

    @GetMapping("/sem1")
    public String sem1Page(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "sem1";
    }

    @GetMapping("/sem2")
    public String sem2Page(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "sem2";
    }

    @GetMapping("/sem3")
    public String sem3Page(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "sem3";
    }

    @GetMapping("/sem4")
    public String sem4Page(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "sem4";
    }

    @GetMapping("/sem5")
    public String sem5Page(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "sem5";
    }

    @GetMapping("/sem6")
    public String sem6Page(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "sem6";
    }

    @GetMapping("/sem7")
    public String sem7Page(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "sem7";
    }

    @GetMapping("/sem8")
    public String sem8Page(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "sem8";
    }

    @GetMapping("/Aimlsem")
    public String Aimlsem(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "Aimlsem";
    }

    @GetMapping("/Mtech")
    public String Mtech(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "Mtech";
    }

    @GetMapping("/BCA")
    public String BCA(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "BCA";
    }

    @GetMapping("/MCA")
    public String MCA(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "MCA";
    }

    @GetMapping("/BBA")
    public String BBA(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "BBA";
    }

    @GetMapping("/MBA")
    public String MBA(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "MBA";
    }

    @GetMapping("/placement")
    public String placement(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        model.addAttribute("previousResults",
                resultRepo.findByEnrollmentOrderByAttemptedAtDesc((String) session.getAttribute("enrollment"))
                        .stream().limit(4).toList()
        );
        return "placement";
    }

    @GetMapping("/placement/aptitude-lab")
    public String aptitudeLab(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "aptitude-lab";
    }

    @GetMapping("/placement/fundamentals-lab")
    public String fundamentalsLab(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "fundamentals-lab";
    }

    @GetMapping("/placement/interview-format")
    public String interviewFormat(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "interview-format";
    }

    @GetMapping("/placement/resume-format")
    public String resumeFormat(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "resume-format";
    }

    @GetMapping("/placement/quiz")
    public String placementQuiz(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";

        setUserData(session, model);
        model.addAttribute("questions", questionRepo.findAllByOrderByCategoryAscDifficultyAscIdDesc());
        model.addAttribute("previousResults",
                resultRepo.findByEnrollmentOrderByAttemptedAtDesc((String) session.getAttribute("enrollment"))
                        .stream().limit(3).toList()
        );
        return "placement-quiz";
    }

    @PostMapping("/placement/quiz/submit")
    public String submitPlacementQuiz(@RequestParam Map<String, String> answers,
                                      HttpSession session,
                                      Model model) {
        if (!checkUser(session)) return "redirect:/login";

        List<PlacementQuestion> questions = questionRepo.findAllByOrderByCategoryAscDifficultyAscIdDesc();
        int correctAnswers = 0;

        for (PlacementQuestion question : questions) {
            String selectedAnswer = answers.get("q" + question.getId());
            if (selectedAnswer != null &&
                    selectedAnswer.equalsIgnoreCase(question.getCorrectOption())) {
                correctAnswers++;
            }
        }

        int totalQuestions = questions.size();
        int scorePercent = totalQuestions == 0 ? 0 :
                (int) Math.round((correctAnswers * 100.0) / totalQuestions);

        PlacementResult result = new PlacementResult();
        result.setName((String) session.getAttribute("name"));
        result.setEnrollment((String) session.getAttribute("enrollment"));
        result.setTotalQuestions(totalQuestions);
        result.setCorrectAnswers(correctAnswers);
        result.setScorePercent(scorePercent);
        result.setAttemptedAt(LocalDateTime.now());
        resultRepo.save(result);
        firebaseSyncService.syncPlacementResult(result);

        setUserData(session, model);
        model.addAttribute("result", result);
        model.addAttribute("questions", questions);
        model.addAttribute("answers", answers);
        return "placement-result";
    }
}
