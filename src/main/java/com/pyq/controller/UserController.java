package com.pyq.controller;

import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import org.springframework.beans.factory.annotation.Autowired;
import com.pyq.model.Feedback;
import com.pyq.model.PlacementQuestion;
import com.pyq.model.PlacementResult;
import com.pyq.repository.PlacementQuestionRepository;
import com.pyq.repository.PlacementResultRepository;
import com.pyq.service.FeedbackService;
import com.pyq.service.FirebaseSyncService;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;

@Controller
public class UserController {

    @Autowired
    private FeedbackService feedbackService;

    @Autowired
    private PlacementQuestionRepository questionRepo;

    @Autowired
    private PlacementResultRepository resultRepo;

    @Autowired
    private FirebaseSyncService firebaseSyncService;

    // ✅ Common methods
    private boolean checkUser(HttpSession session) {
        return session.getAttribute("role") != null &&
                session.getAttribute("role").equals("USER");
    }

    private void setUserData(HttpSession session, Model model) {
        model.addAttribute("name", session.getAttribute("name"));
        model.addAttribute("enrollment", session.getAttribute("enrollment"));
        model.addAttribute("semester", session.getAttribute("semester"));
    }

    // 🔹 Root → redirect to login
    @GetMapping("/")
    public String homeRedirect() {
        return "redirect:/login";
    }

    // 🔹 COURSE PAGE
    @GetMapping("/course")
    public String course(HttpSession session, Model model) {

        // 🔐 SECURITY
        if (session.getAttribute("role") == null ||
                !session.getAttribute("role").equals("USER")) {

            return "redirect:/login";
        }

        // ✅ data set
        model.addAttribute("name", session.getAttribute("name"));
        model.addAttribute("enrollment", session.getAttribute("enrollment"));
        model.addAttribute("semester", session.getAttribute("semester"));
        var results = resultRepo.findByEnrollmentOrderByAttemptedAtDesc((String) session.getAttribute("enrollment"));
        model.addAttribute("recentResults", results.stream().limit(3).toList());
        model.addAttribute("attemptCount", results.size());
        model.addAttribute("bestScore", results.stream().mapToInt(PlacementResult::getScorePercent).max().orElse(0));
        model.addAttribute("latestScore", results.isEmpty() ? 0 : results.get(0).getScorePercent());
        model.addAttribute("questionCount", questionRepo.count());

        return "course";
    }

    // 🔹 SEM PAGE
    @GetMapping("/sem")
    public String sem(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "sem";
    }

    // 🔥 SEMESTER PAGES
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

    // 🔹 AIML
    @GetMapping("/Aimlsem")
    public String Aimlsem(HttpSession session, Model model) {
        if (!checkUser(session)) return "redirect:/login";
        setUserData(session, model);
        return "Aimlsem";
    }

    // 🔹 OTHER COURSES
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

    // 🔹 Placement
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
