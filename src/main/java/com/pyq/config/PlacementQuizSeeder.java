package com.pyq.config;

import com.pyq.model.PlacementQuestion;
import com.pyq.repository.PlacementQuestionRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class PlacementQuizSeeder implements CommandLineRunner {

    private final PlacementQuestionRepository questionRepo;

    public PlacementQuizSeeder(PlacementQuestionRepository questionRepo) {
        this.questionRepo = questionRepo;
    }

    @Override
    public void run(String... args) {
        if (questionRepo.count() > 0) return;

        saveQuestion("Aptitude",
                "If a train running at 60 km/hr crosses a pole in 18 seconds, what is the length of the train?",
                "180 m", "240 m", "300 m", "360 m", "C", "Easy",
                "Speed 60 km/hr is 50/3 m/s. Length = speed x time = 50/3 x 18 = 300 m.");

        saveQuestion("Reasoning",
                "Find the next term in the series: 2, 6, 12, 20, 30, ?",
                "36", "40", "42", "44", "C", "Medium",
                "The differences are 4, 6, 8, 10, so the next difference is 12.");

        saveQuestion("Technical",
                "Which data structure is mainly used in recursion internally?",
                "Queue", "Stack", "Array", "Graph", "B", "Easy",
                "Function calls are stored in the call stack.");

        saveQuestion("Technical",
                "Which SQL command is used to remove all rows from a table but keep the table structure?",
                "DROP", "DELETE DATABASE", "TRUNCATE", "ALTER", "C", "Medium",
                "TRUNCATE removes table rows while keeping the table definition.");

        saveQuestion("HR Interview",
                "Which answer is best when asked about your weakness in an interview?",
                "Say you have no weakness", "Share a real weakness and improvement plan",
                "Blame your college", "Avoid the question", "B", "Easy",
                "A mature answer shows self-awareness and improvement.");
    }

    private void saveQuestion(String category,
                              String question,
                              String optionA,
                              String optionB,
                              String optionC,
                              String optionD,
                              String correctOption,
                              String difficulty,
                              String explanation) {
        PlacementQuestion placementQuestion = new PlacementQuestion();
        placementQuestion.setCategory(category);
        placementQuestion.setQuestion(question);
        placementQuestion.setOptionA(optionA);
        placementQuestion.setOptionB(optionB);
        placementQuestion.setOptionC(optionC);
        placementQuestion.setOptionD(optionD);
        placementQuestion.setCorrectOption(correctOption);
        placementQuestion.setDifficulty(difficulty);
        placementQuestion.setExplanation(explanation);
        questionRepo.save(placementQuestion);
    }
}
