package com.pyq.config;

import com.pyq.model.PlacementQuestion;
import com.pyq.repository.PlacementQuestionRepository;
import org.springframework.data.domain.Sort;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.util.HashSet;
import java.util.Locale;
import java.util.Set;

@Component
public class PlacementQuizSeeder implements CommandLineRunner {

    private final PlacementQuestionRepository questionRepo;
    private Set<String> existingQuestionTexts = new HashSet<>();

    public PlacementQuizSeeder(PlacementQuestionRepository questionRepo) {
        this.questionRepo = questionRepo;
    }

    @Override
    public void run(String... args) {
        existingQuestionTexts = new HashSet<>();
        for (PlacementQuestion question : questionRepo.findAll(Sort.by(Sort.Direction.ASC, "id"))) {
            existingQuestionTexts.add(normalizeQuestion(question.getQuestion()));
        }

        seedAptitudeQuestions();
        seedTechnicalQuestions();
    }

    private void seedAptitudeQuestions() {
        saveQuestion("Aptitude",
                "If a train running at 60 km/hr crosses a pole in 18 seconds, what is the length of the train?",
                "180 m", "240 m", "300 m", "360 m", "C", "Easy",
                "Speed 60 km/hr is 50/3 m/s. Length = speed x time = 50/3 x 18 = 300 m.");

        saveQuestion("Aptitude",
                "Find the next term in the series: 2, 6, 12, 20, 30, ?",
                "36", "40", "42", "44", "C", "Medium",
                "The differences are 4, 6, 8, 10, so the next difference is 12.");

        saveQuestion("Aptitude",
                "A man sells an article for Rs. 920 and gains 15%. What was the cost price?",
                "Rs. 780", "Rs. 800", "Rs. 820", "Rs. 840", "B", "Medium",
                "Cost price = selling price / 1.15 = 920 / 1.15 = 800.");

        saveQuestion("Aptitude",
                "The average of 5 numbers is 24. If one number is removed, the average becomes 22. What is the removed number?",
                "28", "30", "32", "34", "C", "Medium",
                "Total of 5 numbers = 120. Total of remaining 4 numbers = 88. Removed number = 32.");

        saveQuestion("Aptitude",
                "A can complete a work in 12 days and B can complete it in 18 days. In how many days can they complete it together?",
                "6.8 days", "7.2 days", "7.5 days", "8 days", "B", "Medium",
                "Combined work per day = 1/12 + 1/18 = 5/36. Time = 36/5 = 7.2 days.");

        saveQuestion("Aptitude",
                "A sum becomes Rs. 7,260 in 2 years at 10% compound interest annually. What is the principal?",
                "Rs. 5,800", "Rs. 6,000", "Rs. 6,200", "Rs. 6,400", "B", "Medium",
                "Principal = 7260 / 1.21 = 6000.");

        saveQuestion("Aptitude",
                "The ratio of ages of A and B is 3:5. After 8 years, the ratio becomes 5:7. What is A's present age?",
                "10 years", "12 years", "14 years", "16 years", "B", "Medium",
                "Let ages be 3x and 5x. (3x+8)/(5x+8)=5/7 gives x=4, so A is 12.");

        saveQuestion("Aptitude",
                "A boat covers 24 km downstream in 3 hours and 24 km upstream in 6 hours. What is the speed of the stream?",
                "1 km/hr", "2 km/hr", "3 km/hr", "4 km/hr", "B", "Medium",
                "Downstream speed = 8 km/hr, upstream speed = 4 km/hr. Stream speed = (8-4)/2 = 2.");

        saveQuestion("Aptitude",
                "A number is increased by 20% and then decreased by 20%. What is the net change?",
                "No change", "4% increase", "4% decrease", "8% decrease", "C", "Easy",
                "Successive +20% and -20% gives 100 x 1.2 x 0.8 = 96, so 4% decrease.");

        saveQuestion("Aptitude",
                "If 15 men can finish a job in 20 days, how many men are needed to finish it in 12 days?",
                "20", "24", "25", "30", "C", "Easy",
                "Men x days is constant. Required men = 15 x 20 / 12 = 25.");

        saveQuestion("Aptitude",
                "Find the missing number: 4, 9, 19, 39, 79, ?",
                "149", "159", "169", "179", "B", "Medium",
                "Each term is previous x 2 + 1. Next = 79 x 2 + 1 = 159.");

        saveQuestion("Aptitude",
                "A shopkeeper marks an item 40% above cost and gives a 10% discount. What is the profit percentage?",
                "24%", "25%", "26%", "28%", "C", "Medium",
                "Selling price = 140% x 90% = 126% of cost, so profit is 26%.");

        saveQuestion("Aptitude",
                "If SIMPLE is coded as TJNQMF, how is MARKET coded?",
                "NBSLFU", "NBSLDU", "LZQJDS", "NCTLFU", "A", "Easy",
                "Each letter is shifted by one position forward.");

        saveQuestion("Aptitude",
                "In a class, 60% students passed in Math and 70% passed in English. If 50% passed in both, what percent failed in both?",
                "10%", "15%", "20%", "25%", "C", "Medium",
                "Passed in at least one = 60 + 70 - 50 = 80%. Failed in both = 20%.");

        saveQuestion("Aptitude",
                "A person travels 60 km at 30 km/hr and 60 km at 60 km/hr. What is the average speed?",
                "36 km/hr", "40 km/hr", "45 km/hr", "48 km/hr", "B", "Medium",
                "Total distance = 120 km. Total time = 2 + 1 = 3 hours. Average speed = 40 km/hr.");

        saveQuestion("Aptitude",
                "The probability of getting an even number when a die is rolled once is:",
                "1/6", "1/3", "1/2", "2/3", "C", "Easy",
                "Even outcomes are 2, 4, 6. Probability = 3/6 = 1/2.");

        saveQuestion("Aptitude",
                "A pipe fills a tank in 8 hours and another pipe empties it in 12 hours. If both are opened, in how many hours will the tank fill?",
                "18", "20", "22", "24", "D", "Medium",
                "Net filling rate = 1/8 - 1/12 = 1/24 tank per hour.");

        saveQuestion("Aptitude",
                "Find the compound interest on Rs. 10,000 for 2 years at 5% per annum.",
                "Rs. 1,000", "Rs. 1,025", "Rs. 1,050", "Rs. 1,125", "B", "Easy",
                "Amount = 10000 x 1.05 x 1.05 = 11025. Interest = 1025.");

        saveQuestion("Aptitude",
                "A and B invest in the ratio 4:5. After 6 months, A doubles his investment. What is their profit ratio after one year?",
                "5:4", "6:5", "7:6", "8:7", "B", "Hard",
                "A capital months = 4x x 6 + 8x x 6 = 72x. B = 5x x 12 = 60x. Ratio = 6:5.");

        saveQuestion("Aptitude",
                "Choose the word that best completes the sentence: The manager asked the team to be more ___ while handling client data.",
                "careless", "cautious", "casual", "carefree", "B", "Easy",
                "Client data requires careful handling, so cautious is the best fit.");
    }

    private void seedTechnicalQuestions() {
        saveQuestion("Technical",
                "Which data structure is mainly used in recursion internally?",
                "Queue", "Stack", "Array", "Graph", "B", "Easy",
                "Function calls are stored in the call stack.");

        saveQuestion("Technical",
                "Which SQL command is used to remove all rows from a table but keep the table structure?",
                "DROP", "DELETE DATABASE", "TRUNCATE", "ALTER", "C", "Medium",
                "TRUNCATE removes table rows while keeping the table definition.");

        saveQuestion("Technical",
                "What is the time complexity of binary search on a sorted array?",
                "O(n)", "O(log n)", "O(n log n)", "O(1)", "B", "Easy",
                "Binary search halves the search space at every step.");

        saveQuestion("Technical",
                "Which normal form removes partial dependency in a relational database?",
                "1NF", "2NF", "3NF", "BCNF", "B", "Medium",
                "2NF requires 1NF and removal of partial dependency on a composite key.");

        saveQuestion("Technical",
                "In operating systems, which scheduling algorithm can cause starvation?",
                "Round Robin", "FCFS", "Priority Scheduling", "Shortest Job First only with equal burst time", "C", "Medium",
                "Low-priority processes can wait indefinitely in priority scheduling.");

        saveQuestion("Technical",
                "Which protocol is connection-oriented and provides reliable delivery?",
                "UDP", "TCP", "IP", "ARP", "B", "Easy",
                "TCP establishes a connection and ensures reliable ordered delivery.");

        saveQuestion("Technical",
                "Which Java concept allows multiple methods with the same name but different parameter lists?",
                "Inheritance", "Overriding", "Overloading", "Encapsulation", "C", "Easy",
                "Method overloading uses the same method name with different parameters.");

        saveQuestion("Technical",
                "Which data structure is best suited for implementing an LRU cache?",
                "Array and stack", "HashMap and doubly linked list", "Queue only", "Binary search tree only", "B", "Hard",
                "HashMap gives quick lookup and doubly linked list maintains recent-use order.");

        saveQuestion("Technical",
                "What does a foreign key represent in SQL?",
                "A unique row identifier in the same table", "A link to a primary key in another table", "An encrypted column", "A temporary index", "B", "Easy",
                "A foreign key creates a relationship with a key in another table.");

        saveQuestion("Technical",
                "Which OS concept allows multiple processes to appear to run at the same time on a single CPU?",
                "Paging", "Context switching", "Spooling", "Deadlock", "B", "Medium",
                "The CPU switches between processes quickly using context switching.");

        saveQuestion("Technical",
                "Which HTTP status code means resource not found?",
                "200", "301", "404", "500", "C", "Easy",
                "404 indicates that the requested resource was not found.");

        saveQuestion("Technical",
                "Which traversal of a binary search tree returns values in sorted order?",
                "Preorder", "Inorder", "Postorder", "Level order", "B", "Medium",
                "Inorder traversal of a BST visits left, root, and right in sorted order.");

        saveQuestion("Technical",
                "Which Java collection does not allow duplicate elements?",
                "List", "Set", "Queue", "ArrayList", "B", "Easy",
                "Set is designed to store unique elements.");

        saveQuestion("Technical",
                "Which SQL clause is used to filter grouped records?",
                "WHERE", "ORDER BY", "HAVING", "LIMIT", "C", "Medium",
                "HAVING filters results after GROUP BY aggregation.");

        saveQuestion("Technical",
                "What is the worst-case time complexity of quicksort when the pivot choice is consistently poor?",
                "O(n)", "O(log n)", "O(n log n)", "O(n^2)", "D", "Medium",
                "Poor pivots can split arrays into 0 and n-1 elements repeatedly.");

        saveQuestion("Technical",
                "Which layer of the OSI model is responsible for routing packets?",
                "Data Link", "Network", "Transport", "Application", "B", "Easy",
                "The network layer handles logical addressing and routing.");

        saveQuestion("Technical",
                "Which OOP principle hides internal implementation details and exposes only required behavior?",
                "Inheritance", "Polymorphism", "Encapsulation", "Abstraction", "D", "Medium",
                "Abstraction focuses on exposing essential behavior while hiding implementation details.");

        saveQuestion("Technical",
                "Which condition is necessary for deadlock?",
                "Cache miss", "Mutual exclusion", "Low CPU usage", "High bandwidth", "B", "Medium",
                "Mutual exclusion is one of the four Coffman conditions for deadlock.");

        saveQuestion("Technical",
                "Which index structure is commonly used by databases for range queries?",
                "Stack", "B+ Tree", "Queue", "Hash table only", "B", "Hard",
                "B+ Trees keep keys ordered and are efficient for range scans.");

        saveQuestion("Technical",
                "In REST APIs, which HTTP method is usually idempotent for updating a complete resource?",
                "POST", "PUT", "PATCH", "CONNECT", "B", "Medium",
                "PUT is generally idempotent because repeating the same full update produces the same state.");
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
        String questionKey = normalizeQuestion(question);
        if (existingQuestionTexts.contains(questionKey)) {
            return;
        }

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
        existingQuestionTexts.add(questionKey);
    }

    private String normalizeQuestion(String question) {
        if (question == null) {
            return "";
        }

        return question.trim().replaceAll("\\s+", " ").toLowerCase(Locale.ROOT);
    }
}
