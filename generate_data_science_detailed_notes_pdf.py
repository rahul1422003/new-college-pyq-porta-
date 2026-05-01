from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, Spacer, Table, TableStyle

from generate_data_science_notes_pdf import (
    ComparisonDiagram,
    FlowChart,
    WatermarkDocTemplate,
    bullets,
    make_table,
    p,
    styles,
)


OUTPUT = "Data_Science_5_Unit_Detailed_Notes_Rahul_Yadav.pdf"


def para_list(texts, st):
    items = []
    for text in texts:
        items.append(p(text, st["body"]))
        items.append(Spacer(1, 4))
    return items


def long_answer(title, intro, points, st):
    story = [p(title, st["h2"])]
    story += para_list(intro, st)
    story += bullets(points, st["bullet"])
    story.append(Spacer(1, 5))
    return story


def unit1(st):
    story = [p("UNIT 1: Introduction to Data Science, Preprocessing and EDA", st["unit"])]
    story += long_answer(
        "1. Evolution and Meaning of Data Science",
        [
            "Data Science is the systematic study of data to obtain knowledge, patterns and predictions. It combines statistics, computer science, machine learning, data visualization and domain knowledge. In earlier days, organizations mostly used data for record keeping and simple reporting. As the amount of digital data increased, the need for advanced analysis also increased.",
            "The evolution of Data Science started from statistics, where the focus was on sampling, probability and inference. Later, databases and data warehouses made it possible to store large amounts of structured data. Data mining introduced pattern discovery from large datasets. Big data technologies then made it possible to process huge, fast and varied data. Modern Data Science joins all these ideas to solve real-world problems using complete data pipelines.",
        ],
        [
            "It converts raw data into meaningful information and decision support.",
            "It uses both descriptive analysis and predictive modeling.",
            "It helps organizations reduce risk, improve efficiency and personalize services.",
            "It is used in healthcare, banking, education, agriculture, transport and e-commerce.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Phase", "Description", "Exam Example"],
                ["Statistics", "Mathematical analysis of data samples", "Mean, variance, hypothesis testing"],
                ["Database Systems", "Storage and retrieval of structured data", "SQL queries, data warehouse"],
                ["Data Mining", "Finding hidden patterns in large data", "Association rules, clustering"],
                ["Big Data", "Processing large and fast data", "Hadoop, Spark, logs and sensor data"],
                ["Data Science", "End-to-end analysis and prediction", "Fraud detection, recommendation system"],
            ],
            [1.2 * inch, 2.5 * inch, 2.3 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "2. Data Science Roles",
        [
            "A data science project requires people with different responsibilities. These roles may be performed by separate persons in a large company or by the same person in a small organization. The main aim of all roles is to convert data into useful and reliable insight.",
            "A Data Analyst focuses on reports, charts and business questions. A Data Scientist builds statistical and machine learning models. A Data Engineer prepares data pipelines and databases. A Machine Learning Engineer deploys models into applications. A Business Analyst connects technical findings with business decisions.",
        ],
        [
            "<b>Data Analyst:</b> performs cleaning, reporting, dashboarding and basic statistics.",
            "<b>Data Scientist:</b> performs EDA, feature engineering, model building and interpretation.",
            "<b>Data Engineer:</b> builds ETL pipelines, data warehouses and storage systems.",
            "<b>ML Engineer:</b> optimizes, deploys and monitors machine learning models.",
            "<b>Domain Expert:</b> validates whether the result is useful in the real business situation.",
        ],
        st,
    )
    story += [
        p("3. Stages in a Data Science Project", st["h2"]),
        p("A Data Science project follows a structured lifecycle. If the stages are followed properly, the final model becomes more reliable and useful. In exams, this answer should be written with a flow diagram and explanation of each step.", st["body"]),
        FlowChart(["Business Problem", "Data Collection", "Data Cleaning", "EDA", "Feature Engineering", "Model Training", "Evaluation", "Deployment", "Monitoring"]),
    ]
    story += bullets(
        [
            "<b>Problem definition:</b> identify objective, target variable and success criteria.",
            "<b>Data collection:</b> collect data from databases, APIs, surveys, files or sensors.",
            "<b>Data preprocessing:</b> remove missing values, duplicates, errors and inconsistent formats.",
            "<b>EDA:</b> study distributions, correlations, outliers and trends.",
            "<b>Modeling:</b> apply suitable algorithm and train it on data.",
            "<b>Evaluation:</b> test model using metrics such as accuracy, RMSE, precision and recall.",
            "<b>Deployment:</b> integrate model with application or dashboard.",
            "<b>Monitoring:</b> check performance over time and retrain if data changes.",
        ],
        st["bullet"],
    )
    story += long_answer(
        "4. Applications of Data Science",
        [
            "Data Science is useful wherever data is generated. In healthcare, patient records and medical images can be analyzed to predict diseases. In banking, transaction patterns help detect fraud. In education, student marks and attendance can be analyzed to identify weak students early.",
            "In e-commerce, Data Science recommends products based on user behavior. In transport, it helps route optimization and traffic prediction. In agriculture, weather and soil data can be used to predict crop yield. Thus, Data Science improves decision making in almost every field.",
        ],
        [
            "Healthcare: disease prediction, diagnosis support, drug discovery.",
            "Finance: fraud detection, risk analysis, credit scoring.",
            "Education: student performance prediction, learning analytics.",
            "Retail: recommendation system, customer segmentation, demand forecasting.",
            "Government: public policy analysis and smart city planning.",
        ],
        st,
    )
    story += long_answer(
        "5. Data Security Issues",
        [
            "Data security is a major concern because data science projects often use personal, financial or confidential information. If such data is leaked or misused, it can harm users and organizations. Security is not only a technical issue but also an ethical and legal responsibility.",
            "Common data security problems include unauthorized access, weak passwords, unencrypted storage, insecure APIs, accidental sharing of private data and re-identification of anonymized data. A responsible data science project should follow privacy-by-design principles.",
        ],
        [
            "Use encryption for stored data and data transmission.",
            "Apply role-based access control and strong authentication.",
            "Remove or mask personal identifiers whenever possible.",
            "Maintain audit logs to track data access.",
            "Follow legal and ethical rules for data use.",
        ],
        st,
    )
    story += [
        p("6. Data Preprocessing Techniques", st["h2"]),
        p("Data preprocessing is the process of preparing raw data for analysis. Raw data usually contains missing values, duplicate records, wrong formats, noisy values and outliers. If preprocessing is not done, even a good algorithm may produce wrong results.", st["body"]),
        make_table(
            [
                ["Technique", "Detailed Explanation", "Example"],
                ["Cleaning", "Improves data quality by removing errors, missing values, noise and duplicate records.", "Replace missing age with median age."],
                ["Integration", "Combines data from multiple sources into one consistent dataset.", "Merge student marks and attendance tables."],
                ["Transformation", "Changes scale, format or representation of data.", "Normalize salary, encode gender as numbers."],
                ["Reduction", "Reduces data size while preserving useful information.", "Feature selection, PCA, sampling."],
                ["Discretization", "Converts continuous values into categories or intervals.", "Age: child, adult, senior."],
            ],
            [1.1 * inch, 3.4 * inch, 1.7 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "7. Exploratory Data Analysis and Descriptive Statistics",
        [
            "Exploratory Data Analysis is performed before model building. It helps the data scientist understand the nature of data, detect outliers, identify missing values and discover relationships between variables. EDA is mainly done using summary statistics and visualizations.",
            "Descriptive statistics summarize data in numerical form. Mean gives central tendency, standard deviation gives spread, skewness shows symmetry and kurtosis shows peakness or tail behavior. Visual tools such as box plots, pivot tables and heat maps make the patterns easier to understand.",
        ],
        [
            "<b>Mean:</b> average value of observations.",
            "<b>Standard deviation:</b> shows how much values differ from mean.",
            "<b>Skewness:</b> positive or negative asymmetry of data.",
            "<b>Kurtosis:</b> indicates sharpness and tail heaviness of distribution.",
            "<b>Box plot:</b> shows median, quartiles and outliers.",
            "<b>Heat map:</b> uses colors to show correlation or intensity.",
        ],
        st,
    )
    return story


def unit2(st):
    story = [p("UNIT 2: Python for Data Science", st["unit"])]
    story += long_answer(
        "1. Importance of Python in Data Science",
        [
            "Python is one of the most popular languages for Data Science because its syntax is simple, readable and close to English. It supports fast development and has a large ecosystem of libraries for numerical computing, data manipulation, visualization, machine learning and deep learning.",
            "Python also works well with files, databases, web APIs and cloud platforms. This makes it useful for the complete data science lifecycle, from data collection to model deployment. Another advantage is community support; many examples, tutorials and ready-made packages are available.",
        ],
        [
            "Easy to learn and suitable for beginners.",
            "Large libraries such as NumPy, Pandas, Scikit-learn, TensorFlow and PyTorch.",
            "Supports automation, visualization and model deployment.",
            "Works with Jupyter Notebook and Google Colab for interactive analysis.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Package", "Detailed Use"],
                ["NumPy", "Provides n-dimensional arrays, mathematical functions, matrix operations and random number generation."],
                ["Pandas", "Provides Series and DataFrame for tabular data cleaning, grouping, filtering and file handling."],
                ["Scikit-learn", "Provides supervised and unsupervised algorithms, preprocessing tools and evaluation metrics."],
                ["Matplotlib/Seaborn", "Used to create line charts, bar charts, histograms, scatter plots, box plots and heat maps."],
            ],
            [1.5 * inch, 4.7 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "2. Supervised Learning",
        [
            "Supervised learning is a machine learning approach in which the algorithm learns from labeled data. Each training example contains input features and the correct output. The model studies the relationship between inputs and output, and then predicts output for new unseen data.",
            "Supervised learning is divided into regression and classification. Regression predicts a continuous numerical value, such as house price or temperature. Classification predicts a category, such as spam/not spam or pass/fail.",
        ],
        [
            "Requires labeled dataset.",
            "Training data is used to learn a mapping function.",
            "Test data is used to evaluate the model.",
            "Common metrics: accuracy, precision, recall, F1-score, MAE, MSE and RMSE.",
        ],
        st,
    )
    story += [
        ComparisonDiagram("Supervised Learning", ("Regression", "Continuous output"), ("Classification", "Class label")),
        make_table(
            [
                ["Algorithm", "Explanation", "Use Case"],
                ["OLS Regression", "Fits a straight line by minimizing sum of squared errors.", "Predict marks, sales, price."],
                ["Logistic Regression", "Uses sigmoid function to predict probability of classes.", "Spam detection, pass/fail."],
                ["Random Forest", "Combines many decision trees and averages/votes outputs.", "Robust classification and regression."],
                ["Gradient Boosting", "Builds weak learners sequentially and corrects previous errors.", "High accuracy prediction tasks."],
            ],
            [1.4 * inch, 3.2 * inch, 1.6 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. Ordinary Least Squares Regression",
        [
            "Ordinary Least Squares is a common linear regression method. It assumes that the relationship between input variable and output variable can be represented by a straight line. The algorithm finds the best line by minimizing the sum of squared differences between actual and predicted values.",
            "OLS is simple and interpretable. The coefficients show how much the target changes when an input feature changes. However, it may not perform well when the relationship is non-linear or when there are strong outliers.",
        ],
        [
            "Equation form: y = b0 + b1x1 + b2x2 + ... + error.",
            "Objective: minimize squared residuals.",
            "Advantages: simple, fast and explainable.",
            "Limitations: sensitive to outliers and multicollinearity.",
        ],
        st,
    )
    story += long_answer(
        "4. Logistic Regression",
        [
            "Logistic regression is used for classification problems. Although its name contains regression, it predicts the probability of class membership. It uses the sigmoid function to convert linear output into a value between 0 and 1.",
            "For example, if a model predicts probability 0.82 for spam, the email can be classified as spam when the threshold is 0.5. Logistic regression is useful because it is simple, interpretable and effective for binary classification.",
        ],
        [
            "Used for binary and multi-class classification.",
            "Output is probability.",
            "Decision threshold converts probability into class.",
            "Common applications: disease prediction, fraud detection, email spam detection.",
        ],
        st,
    )
    story += long_answer(
        "5. Ensemble Methods and Unsupervised Learning",
        [
            "Ensemble methods combine multiple models to improve prediction accuracy. The idea is that a group of models can perform better than a single model. Bagging trains models independently on different samples and reduces variance. Boosting trains models sequentially and reduces bias.",
            "Unsupervised learning is different because it uses unlabeled data. The algorithm tries to find hidden structure in data. Clustering groups similar records, while dimensionality reduction reduces the number of features.",
        ],
        [
            "Bagging example: Random Forest.",
            "Boosting example: AdaBoost, Gradient Boosting, XGBoost.",
            "Clustering example: customer segmentation using K-Means.",
            "Dimensionality reduction example: PCA for visualization and noise reduction.",
        ],
        st,
    )
    story += [
        p("6. Evolutionary Optimization", st["h2"]),
        p("Evolutionary optimization is inspired by biological evolution. It begins with a population of possible solutions. Each solution is evaluated using a fitness function. Better solutions are selected and combined using crossover. Random mutation introduces variation. This process repeats until a good solution is found.", st["body"]),
        FlowChart(["Initial Population", "Fitness Evaluation", "Selection", "Crossover", "Mutation", "New Population", "Optimal Solution"]),
    ]
    return story


def unit3(st):
    story = [p("UNIT 3: Deep Learning and Time Series Analysis", st["unit"])]
    story += long_answer(
        "1. Deep Learning Basics",
        [
            "Deep learning is a branch of machine learning that uses artificial neural networks with multiple layers. These layers learn features automatically from data. In traditional machine learning, feature extraction often needs human effort, but deep learning can learn low-level and high-level features directly from raw data.",
            "A neural network contains input layer, hidden layers and output layer. Each connection has a weight. During training, the model calculates error and updates weights using backpropagation and optimization algorithms such as gradient descent.",
        ],
        [
            "Useful for image recognition, speech recognition, natural language processing and time series.",
            "Needs large data and high computational power.",
            "Learns hierarchical features automatically.",
            "Common components: neurons, weights, bias, activation function, loss function and optimizer.",
        ],
        st,
    )
    story += [
        FlowChart(["Input Layer", "Hidden Layer 1", "Hidden Layer 2", "Output Layer", "Loss Calculation", "Backpropagation"]),
        Spacer(1, 8),
    ]
    story += long_answer(
        "2. TensorFlow, Keras and PyTorch",
        [
            "TensorFlow is an open-source deep learning framework developed for building and deploying machine learning models. It is suitable for production systems and supports CPUs, GPUs and TPUs. Keras is a high-level API that runs on TensorFlow and makes model building easier.",
            "PyTorch is another popular deep learning framework. It is known for dynamic computation graphs, which make debugging and experimentation easier. Researchers often prefer PyTorch because models can be modified easily during execution.",
        ],
        [
            "TensorFlow: scalable, production-friendly and supports deployment tools.",
            "Keras: simple layer-based API for quick model development.",
            "PyTorch: flexible, research-friendly and easy to debug.",
            "All three support neural networks, CNNs, RNNs and deep learning optimization.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Feature", "TensorFlow/Keras", "PyTorch"],
                ["Ease of Use", "Keras provides very simple model creation.", "Pythonic and flexible for experimentation."],
                ["Graph Type", "Uses static/optimized graph execution.", "Uses dynamic computation graph."],
                ["Best For", "Production deployment and standard workflows.", "Research, NLP and custom model design."],
                ["Deployment", "TensorFlow Serving, Lite, JS.", "TorchScript and deployment tools."],
            ],
            [1.3 * inch, 2.4 * inch, 2.3 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. CNN Architecture",
        [
            "A Convolutional Neural Network is a deep learning model mainly used for image data. It uses convolution filters to detect local patterns such as edges, corners, shapes and textures. Pooling layers reduce the size of feature maps and make the model less sensitive to small changes.",
            "After convolution and pooling, the data is flattened and passed to fully connected layers. The final output layer gives class probabilities. CNNs are widely used in face recognition, object detection, medical imaging and handwritten digit recognition.",
        ],
        [
            "Convolution layer extracts features using filters.",
            "Activation function introduces non-linearity, commonly ReLU.",
            "Pooling layer reduces spatial dimensions.",
            "Fully connected layer performs final classification.",
        ],
        st,
    )
    story += [FlowChart(["Image Input", "Convolution", "ReLU", "Pooling", "Convolution", "Flatten", "Dense Layer", "Prediction"])]
    story += long_answer(
        "4. Style Transfer, Text Generation and Sentiment Analysis",
        [
            "Style transfer is a deep learning technique that combines content from one image with the artistic style of another image. It is commonly performed using CNNs where different layers capture content and style features.",
            "Text generation uses sequence models to predict the next word or character based on previous text. Sentiment analysis is a text classification task that identifies whether a text expresses positive, negative or neutral emotion. PyTorch can be used to build models for both tasks using neural networks and embeddings.",
        ],
        [
            "Style transfer: content image + style image = generated artistic image.",
            "Text generation: learns language pattern and produces new text.",
            "Sentiment analysis: converts text into tokens, embeddings and class labels.",
            "Applications: chatbots, review analysis, creative tools and social media monitoring.",
        ],
        st,
    )
    story += long_answer(
        "5. Time Series Analysis",
        [
            "A time series is a sequence of observations recorded at regular time intervals. Examples include stock prices, rainfall, electricity demand and monthly sales. Time series analysis studies how values change over time and helps forecast future values.",
            "Time series data may contain trend, seasonality, cyclic pattern and random noise. Trend shows long-term movement. Seasonality is a repeating pattern at fixed intervals. Noise is random variation. Before modeling, the data is visualized and checked for stationarity.",
        ],
        [
            "AR model uses past values to predict future value.",
            "MA model uses past forecast errors.",
            "ARMA combines AR and MA for stationary data.",
            "ARIMA adds differencing to handle non-stationary data.",
            "Fourier analysis studies frequency components in signals.",
            "State-space models represent hidden states that change over time.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Term", "Detailed Meaning"],
                ["Stationarity", "Statistical properties such as mean and variance remain constant over time."],
                ["ACF", "Autocorrelation function measures relation with past lags."],
                ["PACF", "Partial autocorrelation helps identify AR order."],
                ["Model Estimation", "Finding best parameter values for selected model."],
                ["Spectral Estimation", "Analysis of signal power at different frequencies."],
            ],
            [1.5 * inch, 4.5 * inch],
        )
    ]
    return story


def unit4(st):
    story = [p("UNIT 4: R for Data Science", st["unit"])]
    story += long_answer(
        "1. Basics of R and RStudio",
        [
            "R is a programming language specially designed for statistical computing and data analysis. It provides many built-in statistical functions and a rich package ecosystem. R is widely used by statisticians, researchers, data analysts and academic institutions.",
            "RStudio is an integrated development environment for R. It provides a script editor, console, environment window, plots window and package manager. It makes R programming easier by organizing all work in one interface.",
        ],
        [
            "R is strong in statistics, visualization and data analysis.",
            "RStudio improves productivity and project organization.",
            "Popular packages: ggplot2, dplyr, tidyr, caret, randomForest.",
            "R supports data import, cleaning, visualization, modeling and reporting.",
        ],
        st,
    )
    story += long_answer(
        "2. R Data Structures",
        [
            "Data structures are used to store and organize data. R provides multiple structures depending on the type and dimensions of data. Choosing the correct data structure makes analysis easier and more efficient.",
            "Vectors store one-dimensional same-type data. Factors store categorical variables. Lists can store different types of objects. Matrices and arrays store same-type data in two or more dimensions. Data frames store tabular data and are most commonly used in data science.",
        ],
        [
            "Vector: c(10, 20, 30), all elements same type.",
            "Factor: categorical values such as Male/Female or Low/Medium/High.",
            "List: can store vector, matrix, model and text together.",
            "Matrix: rows and columns with same data type.",
            "Data frame: table where each column can have a different data type.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Structure", "Dimension", "Data Type", "Use"],
                ["Vector", "1D", "Same type", "Marks, age, salary"],
                ["Factor", "1D", "Categories", "Class labels"],
                ["List", "Mixed", "Different types", "Model results"],
                ["Matrix", "2D", "Same type", "Mathematical operations"],
                ["Array", "Multi-D", "Same type", "Scientific data"],
                ["Data Frame", "2D", "Different columns", "CSV dataset"],
            ],
            [1.2 * inch, 1.0 * inch, 1.5 * inch, 2.3 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. Working with Data in R",
        [
            "Working with data in R begins by importing data from CSV, Excel, databases or web sources. After importing, the analyst inspects structure, dimensions, missing values and summary statistics. Data cleaning is then done to remove errors and make the data ready for analysis.",
            "Visualization is also an important part of R workflow. Base R plotting functions and ggplot2 can create bar charts, histograms, box plots, scatter plots and line charts. These charts help identify patterns before applying machine learning models.",
        ],
        [
            "read.csv() is used to import CSV files.",
            "head(), str(), summary() and dim() inspect data.",
            "is.na() checks missing values.",
            "ggplot2 creates professional visualizations.",
            "dplyr functions filter(), select(), mutate() and summarize() help data manipulation.",
        ],
        st,
    )
    story += [
        FlowChart(["Import Data", "Inspect Data", "Clean Missing Values", "Transform Variables", "Visualize", "Model", "Interpret"]),
        Spacer(1, 8),
    ]
    story += long_answer(
        "4. Regression and Classification with R",
        [
            "R provides many tools for predictive modeling. Linear regression can be implemented using lm(), which estimates the relationship between dependent and independent variables. Logistic regression can be implemented using glm() with binomial family for classification.",
            "For advanced classification, R packages such as caret, randomForest and e1071 can be used. The usual process is to split data into training and testing sets, train the model, make predictions and evaluate the result using appropriate metrics.",
        ],
        [
            "Regression predicts continuous values.",
            "Classification predicts categories.",
            "lm() is used for linear regression.",
            "glm() is used for logistic regression.",
            "caret package gives a unified interface for many models.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Point", "Python", "R"],
                ["Main Strength", "Machine learning, automation and deployment", "Statistics, data analysis and visualization"],
                ["Data Handling", "Pandas DataFrame", "R Data Frame and tidyverse"],
                ["Visualization", "Matplotlib, Seaborn, Plotly", "ggplot2, lattice, plotly"],
                ["Modeling", "Scikit-learn, TensorFlow, PyTorch", "caret, randomForest, glm, lm"],
            ],
            [1.2 * inch, 2.4 * inch, 2.4 * inch],
        )
    ]
    return story


def unit5(st):
    story = [p("UNIT 5: Data Analytics Software and Case Studies", st["unit"])]
    story += long_answer(
        "1. Overview of Data Analytics Software",
        [
            "Data analytics software helps users perform data preparation, visualization, modeling and reporting. Some tools require coding, while others provide graphical interfaces. Such tools are useful for students, analysts and organizations because they reduce time and simplify complex workflows.",
            "Tools such as Weka, Orange and RapidMiner are useful for machine learning without writing much code. Minitab is useful for statistical quality control. Power BI is used for interactive dashboards. GitHub is used for version control and collaboration. Google Colab provides cloud-based notebooks for Python and machine learning.",
        ],
        [
            "They help import and clean data.",
            "They provide visualization and reporting features.",
            "They support machine learning and statistical analysis.",
            "They improve collaboration and reproducibility.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Tool", "Detailed Explanation", "Best Use"],
                ["Weka", "Java-based machine learning tool with GUI for preprocessing, classification, clustering and association rules.", "Teaching and basic ML experiments"],
                ["Orange", "Visual workflow tool for data mining using widgets.", "No-code data analysis"],
                ["RapidMiner", "Complete analytics platform for data preparation, ML and deployment.", "Enterprise analytics workflow"],
                ["Minitab", "Statistical software for quality control and hypothesis testing.", "Statistics and industrial quality"],
                ["Power BI", "Microsoft BI tool for dashboards and interactive reports.", "Business reporting"],
                ["GitHub", "Cloud platform for Git repositories and collaboration.", "Version control and teamwork"],
                ["Google Colab", "Browser-based Python notebook with cloud runtime.", "ML practice and GPU experiments"],
            ],
            [1.0 * inch, 3.8 * inch, 1.4 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "2. Version Control in Data Science Projects",
        [
            "Version control is the process of tracking changes in files over time. In data science, many files change frequently, such as scripts, notebooks, reports and configuration files. Without version control, it becomes difficult to know which model or code version produced a result.",
            "Git is the most common version control tool. GitHub stores Git repositories online and supports collaboration. Teams can create branches, commit changes, review code and merge updates. Version control increases reproducibility and prevents accidental loss of work.",
        ],
        [
            "Tracks history of code and documents.",
            "Allows rollback to previous versions.",
            "Supports teamwork using branches and pull requests.",
            "Improves reproducibility of experiments.",
            "Secrets and private datasets should not be committed.",
        ],
        st,
    )
    story += [FlowChart(["Initialize Git Repo", "Add Project Files", "Commit", "Push to GitHub", "Create Branch", "Review and Merge"])]
    story += long_answer(
        "3. Case Study: Student Performance Prediction",
        [
            "In this case study, the goal is to predict whether a student may perform well or need academic support. Data can be collected from attendance records, internal marks, assignment submissions, previous semester results and quiz performance.",
            "The project starts with cleaning missing values and inconsistent enrollment numbers. EDA is used to find whether attendance and assignment marks are related to final marks. A classification model can predict pass/fail or risk category. The final output may be shown in a dashboard for teachers.",
        ],
        [
            "Input data: attendance, marks, assignments, quizzes.",
            "Problem type: classification or regression.",
            "Models: logistic regression, decision tree, random forest.",
            "Output: student risk level or predicted score.",
            "Benefit: early intervention and better academic planning.",
        ],
        st,
    )
    story += long_answer(
        "4. Case Study: Sales Forecasting",
        [
            "Sales forecasting predicts future sales using historical sales data. The data may include date, product, price, season, festival period and advertisement information. This is a time series problem because observations are recorded over time.",
            "EDA identifies trend and seasonality. ARIMA or regression models can be used for forecasting. The forecast helps businesses manage inventory, plan production and reduce losses due to overstocking or understocking.",
        ],
        [
            "Input data: date-wise sales, product category, price and promotion.",
            "Techniques: ARIMA, regression, moving average.",
            "Visualization: line chart, seasonality plot, forecast plot.",
            "Tool: Python, R, Power BI or Excel.",
            "Benefit: better demand planning and business decisions.",
        ],
        st,
    )
    story += long_answer(
        "5. Case Study: Sentiment Analysis",
        [
            "Sentiment analysis identifies the emotional tone of text. It can be applied to customer reviews, tweets, feedback forms and product comments. The result may be positive, negative or neutral.",
            "The project begins with text preprocessing such as lowercasing, removing punctuation, tokenization and stopword removal. Features can be extracted using TF-IDF or word embeddings. A classifier then predicts sentiment. Companies use this analysis to understand customer satisfaction.",
        ],
        [
            "Input data: reviews, tweets, feedback comments.",
            "Preprocessing: cleaning, tokenization, stopword removal.",
            "Models: Naive Bayes, logistic regression, LSTM, transformer models.",
            "Output: positive, negative or neutral sentiment.",
            "Benefit: customer opinion analysis and product improvement.",
        ],
        st,
    )
    return story


def exam_questions(st):
    story = [p("Important Semester Exam Questions", st["unit"])]
    units = {
        "Unit 1": [
            "Explain Data Science and its evolution in detail.",
            "Describe roles in a Data Science project.",
            "Explain stages in Data Science lifecycle with diagram.",
            "Explain data preprocessing techniques with examples.",
            "Explain EDA and descriptive statistics.",
        ],
        "Unit 2": [
            "Explain Python libraries used in Data Science.",
            "Differentiate supervised and unsupervised learning.",
            "Explain OLS and Logistic Regression in detail.",
            "Explain ensemble methods with examples.",
            "Explain evolutionary optimization.",
        ],
        "Unit 3": [
            "Explain deep learning and neural network architecture.",
            "Compare TensorFlow, Keras and PyTorch.",
            "Explain CNN with diagram.",
            "Explain style transfer, text generation and sentiment analysis.",
            "Explain ARMA, ARIMA and Fourier analysis.",
        ],
        "Unit 4": [
            "Explain R and RStudio.",
            "Explain R data structures with examples.",
            "Explain data import and visualization in R.",
            "Explain regression and classification using R.",
            "Compare Python and R for Data Science.",
        ],
        "Unit 5": [
            "Explain Weka, Orange and RapidMiner.",
            "Explain Power BI, GitHub and Google Colab.",
            "Explain version control in Data Science projects.",
            "Write case study of student performance prediction.",
            "Write case study of sales forecasting or sentiment analysis.",
        ],
    }
    for unit, qs in units.items():
        story.append(p(unit, st["h2"]))
        story += bullets(qs, st["bullet"])
    return story


def build_pdf():
    st = styles()
    doc = WatermarkDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=42,
        leftMargin=42,
        topMargin=42,
        bottomMargin=42,
        title="Detailed Data Science 5 Unit Notes",
        author="Rahul yadav",
    )

    story = [
        Spacer(1, 75),
        p("Data Science", st["title"]),
        p("Detailed 5 Unit Semester Exam Notes", st["title"]),
        p("Expanded theory, tables, diagrams and long-answer points<br/>Watermark: Rahul yadav", st["subtitle"]),
        make_table(
            [
                ["Unit", "Main Topics"],
                ["Unit 1", "Introduction, data science lifecycle, applications, security, preprocessing and EDA"],
                ["Unit 2", "Python, NumPy, Pandas, Scikit-learn, supervised/unsupervised learning and optimization"],
                ["Unit 3", "Deep learning, TensorFlow, Keras, PyTorch, CNN and time series analysis"],
                ["Unit 4", "R, RStudio, R data structures, visualization, regression and classification"],
                ["Unit 5", "Analytics tools, version control and data science case studies"],
            ],
            [1.0 * inch, 5.0 * inch],
        ),
        PageBreak(),
    ]

    all_units = [unit1(st), unit2(st), unit3(st), unit4(st), unit5(st), exam_questions(st)]
    for idx, section in enumerate(all_units):
        story.extend(section)
        if idx != len(all_units) - 1:
            story.append(PageBreak())

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
