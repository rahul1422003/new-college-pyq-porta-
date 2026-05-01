from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Spacer

from generate_data_science_notes_pdf import (
    FlowChart,
    WatermarkDocTemplate,
    bullets,
    make_table,
    p,
    styles,
)


OUTPUT = "Data_Science_Complete_Exam_Notes_Rahul_Yadav.pdf"


class LightWatermarkDocTemplate(WatermarkDocTemplate):
    def afterPage(self):
        canvas = self.canv
        width, height = self.pagesize
        canvas.saveState()
        canvas.setFont("Helvetica-Bold", 52)
        canvas.setFillColor(colors.Color(0.42, 0.46, 0.52, alpha=0.032))
        canvas.translate(width / 2, height / 2)
        canvas.rotate(35)
        canvas.drawCentredString(0, 0, "Rahul yadav")
        canvas.restoreState()

        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#64748b"))
        canvas.drawRightString(width - 42, 24, f"Page {canvas.getPageNumber()}")
        canvas.restoreState()


def para_list(texts, st):
    out = []
    for text in texts:
        out.append(p(text, st["body"]))
        out.append(Spacer(1, 4))
    return out


def long_answer(title, intro, points, st):
    out = [p(title, st["h2"])]
    out += para_list(intro, st)
    out += bullets(points, st["bullet"])
    out.append(Spacer(1, 5))
    return out


def unit1(st):
    story = [p("UNIT 1: Introduction to Data Science, Preprocessing and EDA", st["unit"])]
    story += long_answer(
        "1. Meaning, Scope and Evolution of Data Science",
        [
            "Data Science is an interdisciplinary field that uses scientific methods, statistical techniques, programming, machine learning and domain knowledge to extract meaningful insights from data. It converts raw data into useful information, predictions and decisions. In modern organizations, Data Science is used not only for reporting but also for automation, forecasting and intelligent decision making.",
            "The evolution of Data Science can be understood as a gradual development from statistics to modern AI-based analytics. Initially, data was analyzed using statistical tools and spreadsheets. Later, database systems and data warehouses helped store large datasets. Data mining introduced automatic pattern discovery. Big data technologies enabled processing of huge and fast data. Today, Data Science combines all these with machine learning, deep learning and cloud computing.",
            "Data Science has become important because every field generates data. Business transactions, sensors, mobile apps, social media, healthcare systems, banking systems and educational portals produce large amounts of data. This data has value only when it is cleaned, analyzed and converted into insight.",
        ],
        [
            "Statistics gives mathematical foundation for analysis.",
            "Programming helps clean, process and automate data workflows.",
            "Machine learning helps build predictive models.",
            "Domain knowledge helps interpret results correctly.",
            "Visualization helps communicate insights to decision makers.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Period/Stage", "Main Idea", "Contribution to Data Science"],
                ["Statistics", "Mathematical analysis of data", "Mean, variance, probability, hypothesis testing"],
                ["Database Era", "Structured storage and querying", "SQL, data warehouses and reports"],
                ["Data Mining", "Pattern discovery", "Classification, clustering, association rules"],
                ["Big Data", "Processing large and fast data", "Hadoop, Spark, distributed storage"],
                ["Modern Data Science", "End-to-end insight and prediction", "ML, AI, visualization, deployment"],
            ],
            [1.3 * inch, 2.3 * inch, 2.4 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "2. Data Science Roles",
        [
            "A Data Science project is usually completed by a team because it requires different types of expertise. Some people focus on business understanding, some on data engineering, some on analysis and some on model deployment. In small teams, one person may perform multiple roles.",
            "The Data Analyst focuses on reports, dashboards and business insights. The Data Scientist builds statistical and machine learning models. The Data Engineer creates pipelines and manages storage. The Machine Learning Engineer converts models into production systems. The Business Analyst understands business requirements and communicates results to stakeholders.",
        ],
        [
            "Data Analyst: prepares reports, dashboards and descriptive analysis.",
            "Data Scientist: performs EDA, feature engineering, modeling and interpretation.",
            "Data Engineer: builds ETL pipelines, databases and data lakes.",
            "ML Engineer: deploys and monitors machine learning models.",
            "Domain Expert: validates whether the result is practically meaningful.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Role", "Responsibility", "Tools/Skills"],
                ["Data Analyst", "Reporting, dashboarding, descriptive statistics", "Excel, SQL, Power BI, Python/R"],
                ["Data Scientist", "Model building and insight discovery", "Python, R, ML, statistics"],
                ["Data Engineer", "Data pipelines and storage", "SQL, Spark, ETL, cloud"],
                ["ML Engineer", "Model deployment and optimization", "APIs, Docker, MLOps"],
                ["Business Analyst", "Requirement and decision support", "Domain knowledge, communication"],
            ],
            [1.3 * inch, 2.7 * inch, 2.0 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. Stages in a Data Science Project",
        [
            "A Data Science project follows a lifecycle. The first stage is problem definition, where the objective, target users, expected output and success metric are decided. Without a clear problem statement, the model may solve the wrong problem.",
            "The second stage is data collection. Data can be collected from databases, files, APIs, surveys, sensors or web sources. After collection, data preprocessing is performed to clean missing values, duplicates, noisy values and inconsistent formats. Exploratory Data Analysis then helps understand trends, correlations and outliers.",
            "After EDA, features are selected or engineered and models are trained. The model is evaluated using suitable metrics. If performance is acceptable, it is deployed into a dashboard, API or application. After deployment, monitoring is required because data patterns can change over time.",
        ],
        [
            "Problem definition decides what needs to be solved.",
            "Data collection gathers relevant data.",
            "Preprocessing improves data quality.",
            "EDA identifies patterns and relationships.",
            "Modeling creates predictive or descriptive solution.",
            "Evaluation checks model quality.",
            "Deployment makes the solution usable.",
            "Monitoring ensures performance over time.",
        ],
        st,
    )
    story += [FlowChart(["Problem Definition", "Data Collection", "Preprocessing", "EDA", "Feature Engineering", "Model Building", "Evaluation", "Deployment", "Monitoring"])]
    story += long_answer(
        "4. Applications and Data Security Issues",
        [
            "Data Science is used in almost every field. In healthcare, it can predict disease risk and analyze medical images. In banking, it detects fraud and supports credit scoring. In e-commerce, it recommends products and predicts demand. In education, it predicts student performance and identifies students who need support.",
            "Data security is important because Data Science projects often use sensitive data such as names, phone numbers, health records, financial transactions and user behavior. If data is leaked or misused, it can cause privacy loss, financial loss and legal problems.",
        ],
        [
            "Use encryption for data at rest and in transit.",
            "Use access control and authentication.",
            "Use anonymization or masking for personal data.",
            "Do not collect unnecessary data.",
            "Maintain audit logs and follow ethical data practices.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Field", "Application", "Example"],
                ["Healthcare", "Prediction and diagnosis", "Diabetes prediction"],
                ["Finance", "Risk and fraud analysis", "Credit card fraud detection"],
                ["Retail", "Recommendation and forecasting", "Product recommendation"],
                ["Education", "Student analytics", "Pass/fail prediction"],
                ["Agriculture", "Yield and weather analysis", "Crop yield forecasting"],
            ],
            [1.2 * inch, 2.7 * inch, 2.1 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "5. Data Preprocessing Techniques",
        [
            "Data preprocessing is the process of converting raw data into clean and useful data. It is one of the most important stages because real-world data is incomplete, noisy and inconsistent. Poor quality data leads to poor quality models, even if advanced algorithms are used.",
            "Data cleaning handles missing values, duplicate records, outliers and wrong entries. Data integration combines data from multiple sources. Data transformation converts data into suitable format using scaling, normalization or encoding. Data reduction decreases data size while preserving meaning. Data discretization converts continuous values into intervals.",
        ],
        [
            "Missing values can be removed or filled using mean, median or mode.",
            "Outliers can be detected using box plots or z-score.",
            "Categorical variables can be converted using label encoding or one-hot encoding.",
            "Scaling makes numerical variables comparable.",
            "Feature selection removes irrelevant variables.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Technique", "Purpose", "Example"],
                ["Cleaning", "Improve quality by removing errors", "Remove duplicate student records"],
                ["Integration", "Merge multiple datasets", "Join attendance and marks"],
                ["Transformation", "Change format or scale", "Normalize salary values"],
                ["Reduction", "Reduce size/features", "PCA, sampling"],
                ["Discretization", "Convert numeric to bins", "Age group: young/adult/senior"],
            ],
            [1.4 * inch, 2.5 * inch, 2.1 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "6. Exploratory Data Analysis and Descriptive Statistics",
        [
            "Exploratory Data Analysis is the process of studying data before applying models. It helps understand distributions, missing values, outliers, correlations and patterns. EDA uses both numerical summaries and visual tools.",
            "Descriptive statistics summarize data. Mean gives the average value. Standard deviation measures spread around the mean. Skewness shows whether data is symmetric or tilted toward one side. Kurtosis shows peakness and tail behavior. Box plots show median, quartiles and outliers. Pivot tables summarize data by categories. Heat maps show values or correlations using colors.",
        ],
        [
            "EDA reduces wrong assumptions about data.",
            "It helps identify important variables.",
            "It detects data quality problems.",
            "It supports feature engineering.",
            "It helps communicate data patterns visually.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Term", "Formula/Meaning", "Interpretation"],
                ["Mean", "Sum of values / number of values", "Central average"],
                ["Standard Deviation", "Spread around mean", "High SD means high variation"],
                ["Skewness", "Asymmetry of distribution", "Positive or negative tilt"],
                ["Kurtosis", "Tail heaviness/peakness", "High kurtosis means heavy tails"],
                ["Box Plot", "Median, quartiles, outliers", "Detects spread and outliers"],
                ["Heat Map", "Color-coded matrix", "Shows correlations/intensity"],
            ],
            [1.4 * inch, 2.4 * inch, 2.2 * inch],
        ),
    ]
    return story


def unit2(st):
    story = [p("UNIT 2: Python for Data Science", st["unit"])]
    story += long_answer(
        "1. Python and Important Libraries",
        [
            "Python is widely used in Data Science because it is simple, readable and has a powerful ecosystem of libraries. It supports data collection, cleaning, analysis, visualization, machine learning and deep learning. Python also works well with Jupyter Notebook and Google Colab, which are useful for interactive experimentation.",
            "NumPy provides fast numerical arrays and mathematical operations. Pandas provides Series and DataFrame for tabular data. Scikit-learn provides machine learning algorithms, preprocessing tools and evaluation metrics. Visualization libraries such as Matplotlib and Seaborn help create charts and graphs.",
        ],
        [
            "NumPy is used for arrays, matrices and linear algebra.",
            "Pandas is used for data cleaning and tabular manipulation.",
            "Scikit-learn is used for regression, classification and clustering.",
            "Matplotlib and Seaborn are used for visualization.",
            "Python supports complete data science workflow.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Library", "Main Object/Feature", "Use"],
                ["NumPy", "ndarray", "Numerical computing and matrix operations"],
                ["Pandas", "Series, DataFrame", "Data cleaning, filtering, grouping"],
                ["Scikit-learn", "Estimator API", "ML models and evaluation"],
                ["Matplotlib", "Figure, Axes", "Basic charts and plots"],
                ["Seaborn", "Statistical plots", "Heat maps, pair plots, box plots"],
            ],
            [1.4 * inch, 1.8 * inch, 2.8 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "2. Supervised Learning: Regression and Classification",
        [
            "Supervised learning uses labeled data. The algorithm learns from input-output pairs and predicts output for new data. If the output is continuous, the problem is regression. If the output is a category, the problem is classification.",
            "In regression, examples include predicting house price, sales or marks. In classification, examples include spam detection, disease prediction and pass/fail prediction. The model is trained on training data and tested on unseen test data.",
        ],
        [
            "Regression output is numerical and continuous.",
            "Classification output is a class label.",
            "Training data teaches the model.",
            "Testing data checks generalization.",
            "Metrics must match the problem type.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Aspect", "Regression", "Classification"],
                ["Output", "Continuous value", "Class label"],
                ["Example", "Predict salary", "Spam or not spam"],
                ["Algorithms", "Linear Regression, Random Forest Regressor", "Logistic Regression, SVM, Decision Tree"],
                ["Metrics", "MAE, MSE, RMSE, R2", "Accuracy, Precision, Recall, F1"],
            ],
            [1.2 * inch, 2.4 * inch, 2.4 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. Ordinary Least Squares Regression",
        [
            "Ordinary Least Squares is a linear regression technique. It tries to find the best-fitting line by minimizing the sum of squared differences between actual and predicted values. These differences are called residuals.",
            "OLS is easy to understand and interpret. The coefficient of a feature shows how much the target changes when that feature increases by one unit, assuming other features are constant. However, OLS is sensitive to outliers and may perform poorly for non-linear data.",
        ],
        [
            "Equation: y = b0 + b1x1 + b2x2 + error.",
            "Goal: minimize squared residuals.",
            "Works best when relationship is linear.",
            "Assumes independent errors and low multicollinearity.",
            "Useful for simple prediction and interpretation.",
        ],
        st,
    )
    story += long_answer(
        "4. Logistic Regression, SVM and Ensemble Methods",
        [
            "Logistic Regression is used for classification. It predicts probability using the sigmoid function. If probability is greater than threshold, the sample is assigned to a class. It is useful for binary classification and is easy to interpret.",
            "Support Vector Machine finds the best decision boundary that separates classes with maximum margin. Ensemble methods combine multiple models to improve performance. Random Forest uses bagging, while boosting methods build models sequentially to correct previous errors.",
        ],
        [
            "Logistic Regression outputs probability.",
            "SVM works well in high-dimensional feature spaces.",
            "Random Forest reduces overfitting by averaging many trees.",
            "Boosting improves weak models step by step.",
            "Ensembles are powerful but may be less interpretable.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Algorithm", "Type", "Main Idea"],
                ["Logistic Regression", "Classification", "Uses sigmoid to predict class probability"],
                ["SVM", "Classification/Regression", "Finds maximum margin boundary"],
                ["Decision Tree", "Both", "Splits data using feature rules"],
                ["Random Forest", "Ensemble", "Combines many trees using bagging"],
                ["Gradient Boosting", "Ensemble", "Sequentially improves weak learners"],
            ],
            [1.5 * inch, 1.5 * inch, 3.0 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "5. Unsupervised Learning and Evolutionary Optimization",
        [
            "Unsupervised learning works with unlabeled data. It is used to discover hidden patterns and structures. Clustering groups similar data points. Dimensionality reduction reduces the number of features while preserving useful information.",
            "Evolutionary optimization is inspired by natural evolution. It starts with a population of possible solutions. Each solution is evaluated using a fitness function. Better solutions are selected, combined and mutated to create new solutions. This is useful when the search space is large.",
        ],
        [
            "K-Means is a common clustering algorithm.",
            "Hierarchical clustering creates tree-like grouping.",
            "PCA is used for dimensionality reduction.",
            "Evolutionary techniques use selection, crossover and mutation.",
            "They are useful for complex optimization problems.",
        ],
        st,
    )
    story += [FlowChart(["Initialize Population", "Evaluate Fitness", "Select Parents", "Crossover", "Mutation", "New Population", "Best Solution"])]
    return story


def unit3(st):
    story = [p("UNIT 3: Deep Learning and Time Series Analysis", st["unit"])]
    story += long_answer(
        "1. Deep Learning Fundamentals",
        [
            "Deep Learning is a branch of machine learning based on artificial neural networks with multiple layers. These layers learn representations from data automatically. It is useful for complex data such as images, text, speech and time series.",
            "A neural network contains neurons, weights, bias, activation functions, loss function and optimizer. During training, the model makes predictions, calculates error and updates weights using backpropagation. Deep networks can learn complex non-linear patterns.",
            "Deep learning usually needs large datasets and high computational power. GPUs are often used to speed up training. Although deep learning gives high accuracy, it may be difficult to interpret compared to simpler models.",
        ],
        [
            "Input layer receives data.",
            "Hidden layers learn intermediate features.",
            "Output layer produces prediction.",
            "Activation functions introduce non-linearity.",
            "Loss function measures prediction error.",
            "Optimizer updates weights to reduce loss.",
        ],
        st,
    )
    story += [FlowChart(["Input", "Hidden Layer", "Activation", "Output", "Loss", "Backpropagation", "Updated Weights"])]
    story += long_answer(
        "2. TensorFlow, Keras and PyTorch",
        [
            "TensorFlow is an open-source framework for machine learning and deep learning. It is suitable for large-scale training and production deployment. Keras is a high-level API that simplifies neural network building using layers, models, optimizers and callbacks.",
            "PyTorch is another popular framework. It is known for dynamic computation graphs and easy debugging. Researchers often prefer PyTorch because it is flexible and Python-friendly. Both TensorFlow and PyTorch support GPU acceleration.",
        ],
        [
            "TensorFlow is strong for production and deployment.",
            "Keras is simple and beginner-friendly.",
            "PyTorch is flexible and research-friendly.",
            "All support CNN, RNN, transformers and custom models.",
            "Choice depends on project needs and team skill.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Point", "TensorFlow/Keras", "PyTorch"],
                ["Graph", "Static/optimized execution", "Dynamic graph"],
                ["Ease", "Keras is very simple", "Pythonic and flexible"],
                ["Deployment", "Strong tools like TF Serving/TFLite", "TorchScript and serving tools"],
                ["Use", "Production and standard workflows", "Research and custom models"],
            ],
            [1.2 * inch, 2.4 * inch, 2.4 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. CNN, Style Transfer, Text Generation and Sentiment Analysis",
        [
            "Convolutional Neural Networks are mainly used for image-related tasks. They use filters to detect visual patterns such as edges, corners and textures. Pooling layers reduce the size of feature maps and fully connected layers perform final prediction.",
            "Style transfer uses deep learning to combine content of one image with the style of another image. Text generation creates new text by predicting the next word or character. Sentiment analysis classifies opinions as positive, negative or neutral.",
        ],
        [
            "CNN is useful in image classification and object detection.",
            "Style transfer combines content representation and style representation.",
            "Text generation is used in chatbots and writing assistants.",
            "Sentiment analysis is used in review and social media analysis.",
            "PyTorch can implement image and text deep learning models.",
        ],
        st,
    )
    story += [
        FlowChart(["Image Input", "Convolution", "ReLU", "Pooling", "Flatten", "Dense Layer", "Prediction"]),
        Spacer(1, 8),
    ]
    story += long_answer(
        "4. Time Series Analysis",
        [
            "Time series data is collected in time order. Examples include daily temperature, monthly sales, stock prices and electricity demand. Time series analysis studies patterns over time and forecasts future values.",
            "Important components are trend, seasonality, cyclic variation and noise. Trend is long-term increase or decrease. Seasonality is repeated pattern at fixed intervals. Noise is random variation. Before modeling, time series is plotted and checked for stationarity.",
        ],
        [
            "Trend shows long-term movement.",
            "Seasonality repeats after fixed time period.",
            "Noise is random fluctuation.",
            "Stationarity means mean and variance remain stable.",
            "Forecasting predicts future values.",
        ],
        st,
    )
    story += long_answer(
        "5. ARMA, ARIMA, Fourier Analysis and State Space Models",
        [
            "ARMA combines autoregressive and moving average components. Autoregressive part uses past values, while moving average part uses past errors. ARMA works for stationary time series. ARIMA extends ARMA by adding differencing, which helps make non-stationary data stationary.",
            "Fourier analysis decomposes a signal into frequency components. It is useful when periodic behavior exists. Spectral estimation studies how signal power is distributed over frequency. State-space models represent hidden states that evolve over time and produce observed data.",
        ],
        [
            "AR model uses past values.",
            "MA model uses past errors.",
            "ARIMA uses differencing for non-stationary series.",
            "ACF and PACF help identify model order.",
            "Fourier analysis is useful for periodic signals.",
            "State-space models are useful for hidden dynamic systems.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Model/Concept", "Meaning", "Use"],
                ["AR", "Uses previous values", "Short-term dependence"],
                ["MA", "Uses previous errors", "Noise correction"],
                ["ARMA", "AR + MA", "Stationary time series"],
                ["ARIMA", "ARMA + differencing", "Non-stationary forecasting"],
                ["Fourier", "Frequency decomposition", "Seasonal/periodic signals"],
                ["State Space", "Hidden state representation", "Dynamic systems"],
            ],
            [1.4 * inch, 2.4 * inch, 2.2 * inch],
        ),
    ]
    return story


def unit4(st):
    story = [p("UNIT 4: R for Data Science", st["unit"])]
    story += long_answer(
        "1. R and RStudio",
        [
            "R is a programming language and environment designed for statistical computing, data analysis and visualization. It is widely used in academics, research, statistics and analytics. R has many packages for data manipulation, visualization and machine learning.",
            "RStudio is an integrated development environment for R. It provides console, script editor, plots panel, files panel, package manager and environment viewer. This makes coding, debugging and visualization easier.",
        ],
        [
            "R is strong in statistics and visualization.",
            "RStudio improves productivity and project management.",
            "R packages extend functionality.",
            "R is useful for reports, dashboards and statistical models.",
        ],
        st,
    )
    story += long_answer(
        "2. R Data Structures",
        [
            "Data structures are used to store data in different forms. R provides vectors, factors, lists, arrays, matrices and data frames. Understanding these structures is important because every analysis task requires data to be stored correctly.",
            "A vector stores one-dimensional same-type data. A factor stores categorical data. A list can store different types of elements. A matrix stores two-dimensional same-type data. A data frame stores table-like data where each column can have different type. Data frames are most commonly used in data science.",
        ],
        [
            "Vector: one-dimensional and same data type.",
            "Factor: categorical variable.",
            "List: collection of different objects.",
            "Array: multidimensional same-type data.",
            "Matrix: two-dimensional same-type data.",
            "Data frame: tabular data with columns.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Structure", "Dimension", "Data Type", "Example"],
                ["Vector", "1D", "Same", "c(10,20,30)"],
                ["Factor", "1D", "Categories", "Low, Medium, High"],
                ["List", "Mixed", "Different", "list(name, marks, model)"],
                ["Array", "Multi-D", "Same", "3D numeric data"],
                ["Matrix", "2D", "Same", "Numerical table"],
                ["Data Frame", "2D", "Column-wise different", "CSV dataset"],
            ],
            [1.2 * inch, 1.0 * inch, 1.6 * inch, 2.2 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. Working with Data and Visualization in R",
        [
            "Working with data in R includes importing, inspecting, cleaning, transforming and visualizing data. Data can be imported from CSV, Excel, databases and web sources. After importing, functions like head(), str(), summary() and dim() help understand the dataset.",
            "Visualization helps identify distributions, relationships and outliers. R supports base plotting and advanced visualization using ggplot2. Histograms show distribution, scatter plots show relationship, box plots show spread and outliers, and line charts show trends over time.",
        ],
        [
            "read.csv() imports CSV data.",
            "head() displays first records.",
            "str() shows data structure.",
            "summary() gives descriptive statistics.",
            "ggplot2 creates professional plots.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Chart", "Purpose", "Example Use"],
                ["Histogram", "Distribution of numerical data", "Marks distribution"],
                ["Bar Chart", "Compare categories", "Students per branch"],
                ["Scatter Plot", "Relationship between variables", "Hours studied vs marks"],
                ["Box Plot", "Median, quartiles, outliers", "Salary spread"],
                ["Line Plot", "Trend over time", "Monthly sales"],
            ],
            [1.5 * inch, 2.4 * inch, 2.1 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "4. Regression and Classification with R",
        [
            "R provides built-in and package-based tools for regression and classification. Linear regression can be performed using lm(), which models a continuous target variable. Logistic regression can be performed using glm() with binomial family for binary classification.",
            "For advanced classification, packages like caret, randomForest and e1071 are used. A typical modeling workflow includes importing data, splitting train/test data, training model, predicting and evaluating results.",
        ],
        [
            "Regression predicts continuous values.",
            "Classification predicts categories.",
            "lm() is used for linear regression.",
            "glm() is used for logistic regression.",
            "caret provides common interface for model training.",
        ],
        st,
    )
    story += [FlowChart(["Import Data", "Clean Data", "Split Train/Test", "Train Model", "Predict", "Evaluate", "Interpret"])]
    story += [
        make_table(
            [
                ["Point", "Python", "R"],
                ["Strength", "General-purpose ML and deployment", "Statistics and visualization"],
                ["Data Structure", "Pandas DataFrame", "R Data Frame"],
                ["Visualization", "Matplotlib, Seaborn", "ggplot2"],
                ["Modeling", "Scikit-learn", "caret, lm, glm"],
                ["Users", "Developers and ML engineers", "Statisticians and analysts"],
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
            "Data analytics software helps users process, analyze, visualize and model data. Some tools are code-based, while others provide graphical user interfaces. Such tools are useful because they reduce manual work and make analytics accessible to more users.",
            "Weka, Orange and RapidMiner are popular for machine learning and data mining. Minitab is widely used for statistics and quality control. Power BI is used for business intelligence dashboards. GitHub supports version control and collaboration. Google Colab provides cloud-based notebooks for Python and machine learning.",
        ],
        [
            "Analytics tools simplify data preparation.",
            "They support visualization and reporting.",
            "Some tools support no-code or low-code workflows.",
            "They help share results with stakeholders.",
            "Tool choice depends on task, skill and organization needs.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Tool", "Purpose", "Important Features"],
                ["Weka", "Data mining and ML", "GUI, classification, clustering, preprocessing"],
                ["Orange", "Visual analytics", "Drag-and-drop workflows, widgets"],
                ["RapidMiner", "End-to-end analytics", "Data prep, ML, deployment"],
                ["Minitab", "Statistical analysis", "Quality control, hypothesis testing"],
                ["Power BI", "Business intelligence", "Dashboards, reports, DAX"],
                ["GitHub", "Version control", "Repositories, branches, collaboration"],
                ["Google Colab", "Cloud notebooks", "Python, GPU/TPU, sharing"],
            ],
            [1.2 * inch, 2.1 * inch, 2.7 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "2. Version Control for Data Science Projects",
        [
            "Version control tracks changes in files over time. In Data Science, code, notebooks, reports and configuration files change frequently. Version control helps reproduce results and collaborate safely.",
            "Git is the most common version control system, and GitHub is a popular online platform for hosting repositories. Data Science projects should store scripts, notebooks, README files and model configuration in Git. Large sensitive datasets should not be directly committed.",
        ],
        [
            "Tracks history of code and notebooks.",
            "Allows rollback to older versions.",
            "Supports team collaboration through branches.",
            "Improves reproducibility of experiments.",
            "Secrets and private data must not be committed.",
        ],
        st,
    )
    story += [FlowChart(["Create Repository", "Add Files", "Commit Changes", "Push to GitHub", "Create Branch", "Review", "Merge"])]
    story += long_answer(
        "3. Case Study: Student Performance Prediction",
        [
            "This project predicts student performance using academic and behavioral data. Input variables may include attendance, internal marks, assignment submission, quiz scores, previous semester marks and participation. The target may be final marks, pass/fail or risk category.",
            "The project begins with data collection from college systems. Data is cleaned to handle missing marks and inconsistent enrollment numbers. EDA checks relation between attendance and marks. A classification model like logistic regression or random forest can predict whether a student is at risk. The result can be shown in a dashboard for teachers.",
        ],
        [
            "Problem type: classification or regression.",
            "Data: attendance, marks, assignments, quizzes.",
            "Models: logistic regression, decision tree, random forest.",
            "Output: risk level or predicted marks.",
            "Benefit: early support for weak students.",
        ],
        st,
    )
    story += long_answer(
        "4. Case Study: Sales Forecasting",
        [
            "Sales forecasting predicts future demand using historical sales data. The data may contain date, product, store, price, discount, festival season and advertising information. Since the data is time-based, time series methods are commonly used.",
            "EDA is performed to identify trend and seasonality. ARIMA, moving average or regression models can be used. Forecasting helps businesses manage inventory, plan marketing and reduce stock problems. Power BI dashboards can show actual sales, predicted sales and category-wise trends.",
        ],
        [
            "Problem type: time series forecasting.",
            "Data: date-wise sales, product, price, discount.",
            "Models: ARIMA, regression, moving average.",
            "Visualization: line chart and forecast plot.",
            "Benefit: better inventory and business planning.",
        ],
        st,
    )
    story += long_answer(
        "5. Case Study: Sentiment Analysis",
        [
            "Sentiment analysis identifies opinion from text data. It can be applied to product reviews, social media posts, feedback forms and support tickets. The output is usually positive, negative or neutral sentiment.",
            "The project starts with text cleaning, tokenization and stopword removal. Text is converted into numerical features using TF-IDF or embeddings. A classification model such as Naive Bayes, Logistic Regression or deep learning model is trained. Results help companies understand customer satisfaction.",
        ],
        [
            "Problem type: text classification.",
            "Data: reviews, comments, tweets or feedback.",
            "Preprocessing: cleaning, tokenization, stopword removal.",
            "Models: Naive Bayes, Logistic Regression, LSTM.",
            "Benefit: customer opinion and product improvement.",
        ],
        st,
    )
    return story


def quick_revision(st):
    story = [p("Quick Revision: Definitions and Differences", st["unit"])]
    story += [
        make_table(
            [
                ["Term", "Exam Definition"],
                ["Data Science", "Field that extracts insights and predictions from data using statistics, programming and domain knowledge."],
                ["EDA", "Process of exploring data using statistics and visualizations before modeling."],
                ["Data Cleaning", "Removing or correcting errors, missing values, duplicates and noisy data."],
                ["Regression", "Supervised learning technique to predict continuous values."],
                ["Classification", "Supervised learning technique to predict class labels."],
                ["Clustering", "Unsupervised learning technique to group similar data points."],
                ["Deep Learning", "Machine learning based on multilayer neural networks."],
                ["Time Series", "Data collected in time order."],
                ["Power BI", "Business intelligence tool for dashboards and reports."],
                ["Version Control", "Tracking and managing changes in project files."],
            ],
            [1.5 * inch, 4.7 * inch],
        ),
        Spacer(1, 8),
        p("Important Comparisons", st["h2"]),
        make_table(
            [
                ["Comparison", "Point 1", "Point 2"],
                ["Data Mining vs Data Science", "Data mining finds patterns", "Data Science includes full lifecycle and prediction"],
                ["R vs Python", "R is strong in statistics", "Python is strong in ML and deployment"],
                ["ARMA vs ARIMA", "ARMA needs stationary data", "ARIMA handles non-stationary data using differencing"],
                ["BoW-like sparse features vs Embeddings", "Sparse features are simple", "Embeddings capture meaning better"],
                ["Dashboard vs Report", "Dashboard is interactive", "Report is usually static"],
            ],
            [1.7 * inch, 2.2 * inch, 2.3 * inch],
        ),
    ]
    return story


def questions(st):
    story = [p("Important Semester Exam Questions", st["unit"])]
    data = {
        "Unit 1": [
            "Explain evolution of Data Science in detail.",
            "Explain roles in a Data Science project.",
            "Explain stages of Data Science lifecycle with diagram.",
            "Explain data preprocessing techniques.",
            "Explain descriptive statistics and EDA tools.",
        ],
        "Unit 2": [
            "Explain Python libraries used in Data Science.",
            "Differentiate regression and classification.",
            "Explain Ordinary Least Squares Regression.",
            "Explain Logistic Regression, SVM and Ensemble Methods.",
            "Explain unsupervised learning and evolutionary optimization.",
        ],
        "Unit 3": [
            "Explain deep learning and neural network architecture.",
            "Compare TensorFlow, Keras and PyTorch.",
            "Explain CNN with diagram.",
            "Explain time series components and forecasting.",
            "Explain ARMA, ARIMA, Fourier analysis and state-space models.",
        ],
        "Unit 4": [
            "Explain R and RStudio.",
            "Explain R data structures with examples.",
            "Explain importing and visualizing data in R.",
            "Explain regression and classification in R.",
            "Compare Python and R for Data Science.",
        ],
        "Unit 5": [
            "Explain Weka, Orange, RapidMiner and Minitab.",
            "Explain Power BI, GitHub and Google Colab.",
            "Explain version control in Data Science projects.",
            "Write a case study on student performance prediction.",
            "Write a case study on sales forecasting or sentiment analysis.",
        ],
    }
    for unit, qs in data.items():
        story.append(p(unit, st["h2"]))
        story += bullets(qs, st["bullet"])
    story.append(p("How to Write Long Answers in Exam", st["h2"]))
    story += bullets(
        [
            "Start with a clear definition.",
            "Draw a diagram or flowchart whenever possible.",
            "Write 4-6 explained points.",
            "Add a table/comparison for theory questions.",
            "End with example or application.",
        ],
        st["bullet"],
    )
    return story


def build_pdf():
    st = styles()
    doc = LightWatermarkDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=42,
        leftMargin=42,
        topMargin=42,
        bottomMargin=42,
        title="Complete Data Science Exam Notes",
        author="Rahul yadav",
    )
    story = [
        Spacer(1, 70),
        p("Data Science", st["title"]),
        p("Complete 5 Unit Semester Exam Notes", st["title"]),
        p("Detailed theory, diagrams, tables, short notes and important questions<br/>Watermark: Rahul yadav", st["subtitle"]),
        make_table(
            [
                ["Unit", "Coverage"],
                ["Unit 1", "Introduction, lifecycle, applications, security, preprocessing and EDA"],
                ["Unit 2", "Python libraries, supervised/unsupervised learning, regression, classification and optimization"],
                ["Unit 3", "Deep learning, frameworks, CNN, style transfer, text generation and time series"],
                ["Unit 4", "R, RStudio, data structures, visualization, regression and classification"],
                ["Unit 5", "Analytics tools, version control and case studies"],
            ],
            [1.0 * inch, 5.0 * inch],
        ),
        PageBreak(),
    ]
    sections = [unit1(st), unit2(st), unit3(st), unit4(st), unit5(st), quick_revision(st), questions(st)]
    for idx, section in enumerate(sections):
        story.extend(section)
        if idx != len(sections) - 1:
            story.append(PageBreak())
    doc.build(story)


if __name__ == "__main__":
    build_pdf()
