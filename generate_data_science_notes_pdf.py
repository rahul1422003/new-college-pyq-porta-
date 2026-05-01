from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Flowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT = "Data_Science_5_Unit_Notes_Rahul_Yadav.pdf"


class WatermarkDocTemplate(SimpleDocTemplate):
    def afterPage(self):
        canvas = self.canv
        width, height = self.pagesize
        canvas.saveState()
        canvas.setFont("Helvetica-Bold", 54)
        canvas.setFillColor(colors.Color(0.35, 0.40, 0.48, alpha=0.045))
        canvas.translate(width / 2, height / 2)
        canvas.rotate(35)
        canvas.drawCentredString(0, 0, "Rahul yadav")
        canvas.restoreState()

        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#64748b"))
        canvas.drawRightString(width - 42, 24, f"Page {canvas.getPageNumber()}")
        canvas.restoreState()


class FlowChart(Flowable):
    def __init__(self, labels, width=450, box_height=30, gap=15):
        super().__init__()
        self.labels = labels
        self.width = width
        self.box_height = box_height
        self.gap = gap
        self.height = len(labels) * box_height + (len(labels) - 1) * gap

    def wrap(self, avail_width, avail_height):
        self.width = min(self.width, avail_width)
        return self.width, self.height

    def draw(self):
        c = self.canv
        box_width = self.width * 0.78
        x = (self.width - box_width) / 2
        y = self.height - self.box_height

        for i, label in enumerate(self.labels):
            c.setFillColor(colors.HexColor("#eff6ff"))
            c.setStrokeColor(colors.HexColor("#2563eb"))
            c.roundRect(x, y, box_width, self.box_height, 7, fill=1, stroke=1)
            c.setFillColor(colors.HexColor("#0f172a"))
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(self.width / 2, y + 10, label)

            if i < len(self.labels) - 1:
                cx = self.width / 2
                c.setStrokeColor(colors.HexColor("#2563eb"))
                c.line(cx, y, cx, y - self.gap + 4)
                c.line(cx, y - self.gap + 4, cx - 4, y - self.gap + 10)
                c.line(cx, y - self.gap + 4, cx + 4, y - self.gap + 10)
            y -= self.box_height + self.gap


class ComparisonDiagram(Flowable):
    def __init__(self, title, left, right, width=450):
        super().__init__()
        self.title = title
        self.left = left
        self.right = right
        self.width = width
        self.height = 92

    def wrap(self, avail_width, avail_height):
        self.width = min(self.width, avail_width)
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(colors.HexColor("#0f172a"))
        c.drawCentredString(self.width / 2, 78, self.title)

        box_w = (self.width - 34) / 2
        c.setFillColor(colors.HexColor("#f0fdf4"))
        c.setStrokeColor(colors.HexColor("#16a34a"))
        c.roundRect(8, 22, box_w, 44, 7, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#ecfeff"))
        c.setStrokeColor(colors.HexColor("#0891b2"))
        c.roundRect(26 + box_w, 22, box_w, 44, 7, fill=1, stroke=1)

        c.setFillColor(colors.HexColor("#0f172a"))
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(8 + box_w / 2, 47, self.left[0])
        c.drawCentredString(26 + box_w + box_w / 2, 47, self.right[0])
        c.setFont("Helvetica", 8)
        c.drawCentredString(8 + box_w / 2, 34, self.left[1])
        c.drawCentredString(26 + box_w + box_w / 2, 34, self.right[1])


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            textColor=colors.HexColor("#0f172a"),
            alignment=TA_CENTER,
            spaceAfter=12,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["Normal"],
            fontSize=10,
            leading=15,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#475569"),
            spaceAfter=18,
        ),
        "unit": ParagraphStyle(
            "unit",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=15,
            textColor=colors.white,
            backColor=colors.HexColor("#1d4ed8"),
            borderPadding=8,
            spaceBefore=8,
            spaceAfter=10,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontSize=12,
            textColor=colors.HexColor("#1e3a8a"),
            spaceBefore=8,
            spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["BodyText"],
            fontSize=9,
            leading=13,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#111827"),
            spaceAfter=5,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=base["BodyText"],
            fontSize=9,
            leading=13,
            leftIndent=12,
            firstLineIndent=-8,
            spaceAfter=3,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["BodyText"],
            fontSize=8,
            leading=11,
            textColor=colors.HexColor("#334155"),
        ),
    }


def p(text, style):
    return Paragraph(text, style)


def bullets(items, style):
    return [p(f"- {item}", style) for item in items]


def make_table(data, col_widths=None):
    tbl = Table(data, colWidths=col_widths, repeatRows=1)
    tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dbeafe")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("LEADING", (0, 0), (-1, -1), 10),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cbd5e1")),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return tbl


def unit_1(st):
    story = [p("UNIT 1: Introduction to Data Science, Preprocessing and EDA", st["unit"])]
    story += [
        p("1. Evolution of Data Science", st["h2"]),
        p(
            "Data Science is an interdisciplinary field that uses statistics, programming, database systems, machine learning and domain knowledge to extract useful insights from data. It evolved from statistics, data mining and business intelligence. Earlier organizations mainly stored and reported data; now they predict outcomes and automate decisions using data-driven models.",
            st["body"],
        ),
        make_table(
            [
                ["Stage", "Main Focus", "Example"],
                ["Statistics", "Summarize and infer from samples", "Mean, variance, hypothesis testing"],
                ["Data Mining", "Discover hidden patterns", "Market basket analysis"],
                ["Big Data", "Handle volume, velocity and variety", "Logs, social media, sensor data"],
                ["Data Science", "End-to-end insight and prediction", "Recommendation system, fraud detection"],
            ],
            [1.2 * inch, 2.4 * inch, 2.4 * inch],
        ),
        Spacer(1, 8),
        p("2. Data Science Roles", st["h2"]),
    ]
    story += bullets(
        [
            "<b>Data Analyst:</b> cleans data, creates reports and dashboards.",
            "<b>Data Scientist:</b> builds predictive models and explains insights.",
            "<b>Data Engineer:</b> designs pipelines, databases and data warehouses.",
            "<b>ML Engineer:</b> deploys machine learning models into applications.",
            "<b>Business Analyst:</b> converts business problems into data questions.",
        ],
        st["bullet"],
    )
    story += [
        p("3. Stages in a Data Science Project", st["h2"]),
        FlowChart(["Problem Definition", "Data Collection", "Data Cleaning", "EDA", "Model Building", "Evaluation", "Deployment and Monitoring"]),
        Spacer(1, 8),
        p("4. Applications of Data Science", st["h2"]),
    ]
    story += bullets(
        [
            "Healthcare: disease prediction, medical image analysis, drug discovery.",
            "Banking: fraud detection, credit scoring, customer segmentation.",
            "Education: student performance prediction and learning analytics.",
            "E-commerce: recommendation systems and demand forecasting.",
            "Agriculture: crop yield prediction and weather-based decision support.",
        ],
        st["bullet"],
    )
    story += [
        p("5. Data Security Issues", st["h2"]),
        p(
            "Data science projects often use personal and sensitive data. Major risks include unauthorized access, data leakage, re-identification of anonymized users, biased decision making and insecure cloud storage. Security controls include encryption, authentication, access control, anonymization, audit logs and ethical data use.",
            st["body"],
        ),
        p("6. Data Preprocessing", st["h2"]),
        make_table(
            [
                ["Technique", "Meaning", "Common Methods"],
                ["Data Cleaning", "Remove errors and improve quality", "Handle missing values, remove duplicates, correct outliers"],
                ["Data Integration", "Combine data from many sources", "Schema matching, entity resolution"],
                ["Data Transformation", "Convert data into useful format", "Normalization, scaling, encoding"],
                ["Data Reduction", "Reduce size without losing meaning", "Sampling, PCA, feature selection"],
                ["Data Discretization", "Convert continuous values into intervals", "Binning, histogram analysis"],
            ],
            [1.4 * inch, 2.2 * inch, 2.4 * inch],
        ),
        Spacer(1, 8),
        p("7. Exploratory Data Analysis (EDA)", st["h2"]),
        p(
            "EDA is the process of understanding data before modeling. It uses descriptive statistics and visual tools to detect patterns, trends, missing values, outliers and relationships among variables.",
            st["body"],
        ),
        make_table(
            [
                ["EDA Tool", "Purpose"],
                ["Mean", "Average value of a variable"],
                ["Standard Deviation", "Spread of data around the mean"],
                ["Skewness", "Asymmetry of distribution"],
                ["Kurtosis", "Sharpness or heaviness of tails"],
                ["Box Plot", "Shows median, quartiles and outliers"],
                ["Pivot Table", "Summarizes data by rows and columns"],
                ["Heat Map", "Shows values or correlations using colors"],
            ],
            [2.0 * inch, 4.0 * inch],
        ),
    ]
    return story


def unit_2(st):
    story = [p("UNIT 2: Python for Data Science", st["unit"])]
    story += [
        p("1. Role of Python in Data Science", st["h2"]),
        p(
            "Python is widely used in data science because it is easy to read, has strong libraries, supports visualization, and integrates well with machine learning frameworks.",
            st["body"],
        ),
        make_table(
            [
                ["Library", "Use"],
                ["NumPy", "Numerical arrays, matrix operations and linear algebra"],
                ["Pandas", "DataFrames, cleaning, grouping and file handling"],
                ["Scikit-learn", "Machine learning models, preprocessing and metrics"],
                ["Matplotlib/Seaborn", "Graphs, charts and statistical visualization"],
            ],
            [1.7 * inch, 4.3 * inch],
        ),
        Spacer(1, 8),
        p("2. NumPy, Pandas and Scikit-learn Review", st["h2"]),
    ]
    story += bullets(
        [
            "NumPy stores homogeneous numerical data in fast n-dimensional arrays.",
            "Pandas stores tabular data in Series and DataFrame objects.",
            "Scikit-learn provides a standard workflow: import model, fit, predict and evaluate.",
        ],
        st["bullet"],
    )
    story += [
        p("3. Supervised Learning", st["h2"]),
        p(
            "Supervised learning uses labeled data. The model learns the relationship between input features and known output labels. It is mainly divided into regression and classification.",
            st["body"],
        ),
        ComparisonDiagram(
            "Supervised Learning Types",
            ("Regression", "Predicts continuous value"),
            ("Classification", "Predicts class label"),
        ),
        make_table(
            [
                ["Algorithm", "Type", "Use"],
                ["Ordinary Least Squares Regression", "Regression", "Predict continuous target by minimizing squared error"],
                ["Logistic Regression", "Classification", "Predict probability of class membership"],
                ["Decision Tree", "Both", "Splits data using feature-based rules"],
                ["Random Forest", "Ensemble", "Combines many decision trees to improve accuracy"],
                ["Gradient Boosting", "Ensemble", "Builds models sequentially to reduce previous errors"],
            ],
            [1.8 * inch, 1.2 * inch, 3.0 * inch],
        ),
        Spacer(1, 8),
        p("4. Ensemble Methods", st["h2"]),
        p(
            "Ensemble methods combine multiple models to produce a stronger model. Bagging reduces variance by training models independently. Boosting reduces bias by training models sequentially.",
            st["body"],
        ),
        p("5. Unsupervised Learning", st["h2"]),
        p(
            "Unsupervised learning works on unlabeled data. It discovers hidden structures such as groups, patterns or reduced representations. Common methods include K-Means clustering, hierarchical clustering and PCA.",
            st["body"],
        ),
        p("6. Optimization Using Evolutionary Techniques", st["h2"]),
        p(
            "Evolutionary techniques are inspired by natural selection. A population of possible solutions is improved using selection, crossover and mutation. These techniques are useful when the search space is large and traditional optimization is difficult.",
            st["body"],
        ),
        FlowChart(["Initialize Population", "Evaluate Fitness", "Selection", "Crossover", "Mutation", "Best Solution"]),
    ]
    return story


def unit_3(st):
    story = [p("UNIT 3: Deep Learning and Time Series Analysis", st["unit"])]
    story += [
        p("1. Deep Learning Overview", st["h2"]),
        p(
            "Deep learning is a branch of machine learning based on artificial neural networks with many layers. It is powerful for images, speech, text and sequence data because it can learn complex features automatically.",
            st["body"],
        ),
        p("2. TensorFlow and Keras", st["h2"]),
        p(
            "TensorFlow is an open-source deep learning framework. Keras is a high-level API that makes model building easier by using layers, optimizers, losses and callbacks.",
            st["body"],
        ),
        p("3. PyTorch", st["h2"]),
        p(
            "PyTorch is a deep learning framework known for dynamic computation graphs and easy debugging. It is widely used in research and production for computer vision and natural language processing.",
            st["body"],
        ),
        make_table(
            [
                ["Framework", "Strength", "Common Use"],
                ["TensorFlow", "Production deployment and scalability", "Web/mobile ML, large production systems"],
                ["Keras", "Simple and fast model design", "Learning, prototypes, standard neural networks"],
                ["PyTorch", "Flexible research and debugging", "NLP, image tasks, research models"],
            ],
            [1.4 * inch, 2.3 * inch, 2.3 * inch],
        ),
        Spacer(1, 8),
        p("4. CNN Overview", st["h2"]),
        p(
            "Convolutional Neural Networks are mainly used for image data. Convolution layers extract features, pooling layers reduce dimensions, and fully connected layers perform classification.",
            st["body"],
        ),
        FlowChart(["Input Image", "Convolution", "Activation", "Pooling", "Flatten", "Fully Connected", "Output Class"]),
        Spacer(1, 8),
        p("5. Style Transfer, Text Generation and Sentiment Analysis", st["h2"]),
    ]
    story += bullets(
        [
            "Style transfer combines content of one image with artistic style of another image.",
            "Text generation predicts next words or characters using sequence models.",
            "Sentiment analysis classifies text as positive, negative or neutral.",
        ],
        st["bullet"],
    )
    story += [
        p("6. Time Series Analysis", st["h2"]),
        p(
            "A time series is data collected over time such as stock prices, temperature or sales. Time series analysis studies trend, seasonality, cycles and noise to forecast future values.",
            st["body"],
        ),
        make_table(
            [
                ["Concept", "Meaning"],
                ["Trend", "Long-term upward or downward movement"],
                ["Seasonality", "Regular repeating pattern"],
                ["Noise", "Random variation"],
                ["ARMA", "Combines autoregressive and moving average components"],
                ["ARIMA", "ARMA with differencing for non-stationary data"],
                ["Fourier Analysis", "Breaks signal into frequency components"],
                ["State Space Model", "Represents hidden state changing over time"],
            ],
            [1.7 * inch, 4.3 * inch],
        ),
        Spacer(1, 8),
        p("7. Model Identification and Estimation", st["h2"]),
        p(
            "Model identification selects a suitable model structure. Estimation finds model parameters. For ARIMA, ACF and PACF plots help choose p, d and q values. Model quality is checked using residual analysis and error metrics.",
            st["body"],
        ),
    ]
    return story


def unit_4(st):
    story = [p("UNIT 4: R for Data Science", st["unit"])]
    story += [
        p("1. Basics of R and RStudio", st["h2"]),
        p(
            "R is a programming language designed for statistical computing, data analysis and visualization. RStudio is an IDE that provides script editor, console, plots, environment and package management.",
            st["body"],
        ),
        p("2. R Data Structures", st["h2"]),
        make_table(
            [
                ["Structure", "Description", "Example Use"],
                ["Vector", "One-dimensional same-type data", "Marks of students"],
                ["Factor", "Categorical data", "Gender, grade, class label"],
                ["List", "Collection of different types", "Model output"],
                ["Array", "Multi-dimensional same-type data", "3D numerical data"],
                ["Matrix", "Two-dimensional same-type data", "Linear algebra"],
                ["Data Frame", "Tabular data with columns", "CSV dataset"],
            ],
            [1.3 * inch, 2.4 * inch, 2.3 * inch],
        ),
        Spacer(1, 8),
        p("3. Working with Data in R", st["h2"]),
    ]
    story += bullets(
        [
            "Import CSV using read.csv() or readr::read_csv().",
            "Inspect data using head(), str(), summary() and dim().",
            "Clean missing values using is.na(), na.omit() or imputation.",
            "Visualize data using base R plots or ggplot2.",
        ],
        st["bullet"],
    )
    story += [
        p("4. Data Visualization in R", st["h2"]),
        make_table(
            [
                ["Chart", "Purpose"],
                ["Bar Chart", "Compare categories"],
                ["Histogram", "Show distribution of numerical variable"],
                ["Scatter Plot", "Show relationship between two variables"],
                ["Box Plot", "Show spread, median and outliers"],
                ["Line Plot", "Show trend over time"],
            ],
            [1.5 * inch, 4.5 * inch],
        ),
        Spacer(1, 8),
        p("5. Regression and Classification with R", st["h2"]),
        p(
            "R supports regression and classification using built-in functions and packages. Linear regression can be built using lm(), logistic regression using glm(), and classification models using packages such as caret, randomForest and e1071.",
            st["body"],
        ),
        FlowChart(["Import Data", "Clean Data", "Split Train/Test", "Build Model", "Predict", "Evaluate"]),
        Spacer(1, 8),
        p("Python vs R", st["h2"]),
        make_table(
            [
                ["Point", "Python", "R"],
                ["Best For", "General programming and ML deployment", "Statistics and visualization"],
                ["Libraries", "NumPy, Pandas, Scikit-learn", "dplyr, ggplot2, caret"],
                ["Users", "Developers and data scientists", "Statisticians and researchers"],
                ["Deployment", "Strong production ecosystem", "Strong analysis/reporting ecosystem"],
            ],
            [1.2 * inch, 2.4 * inch, 2.4 * inch],
        ),
    ]
    return story


def unit_5(st):
    story = [p("UNIT 5: Overview of Data Analytics Software", st["unit"])]
    story += [
        p("1. Need for Analytics Software", st["h2"]),
        p(
            "Analytics software helps users clean, visualize, model and share data. Many tools provide graphical interfaces so that users can perform data analysis with less coding.",
            st["body"],
        ),
        make_table(
            [
                ["Tool", "Main Purpose", "Important Feature"],
                ["Weka", "Machine learning and data mining", "GUI for classification, clustering and preprocessing"],
                ["Orange", "Visual data mining", "Workflow-based drag-and-drop interface"],
                ["RapidMiner", "End-to-end analytics", "Data preparation, modeling and deployment"],
                ["Minitab", "Statistical analysis", "Quality control and hypothesis testing"],
                ["Power BI", "Business intelligence", "Interactive dashboards and reports"],
                ["GitHub", "Code hosting and collaboration", "Version control, issues and pull requests"],
                ["Google Colab", "Cloud notebooks", "Python execution with free GPU/TPU support"],
            ],
            [1.2 * inch, 2.3 * inch, 2.5 * inch],
        ),
        Spacer(1, 8),
        p("2. Version Controlling Tools for Data Science", st["h2"]),
        p(
            "Version control tracks changes in code, notebooks, data processing scripts and documentation. Git is the most common version control system, and GitHub is a popular hosting platform.",
            st["body"],
        ),
        FlowChart(["Create Repository", "Add Files", "Commit Changes", "Push to GitHub", "Collaborate", "Track Versions"]),
        Spacer(1, 8),
        p("3. Good Practices for Data Science Projects", st["h2"]),
    ]
    story += bullets(
        [
            "Keep raw data separate from processed data.",
            "Use clear folder structure: data, notebooks, src, models and reports.",
            "Write README files explaining project goal, setup and results.",
            "Use Git for code and configuration files.",
            "Do not commit passwords, secret keys or private data.",
            "Save model versions and evaluation metrics.",
        ],
        st["bullet"],
    )
    story += [
        p("4. Case Study 1: Student Performance Prediction", st["h2"]),
        p(
            "Goal: predict whether a student may pass or need support. Data can include attendance, marks, assignment completion and previous results. Steps include data cleaning, EDA, feature selection, model building, evaluation and dashboard reporting.",
            st["body"],
        ),
        p("5. Case Study 2: Sales Forecasting", st["h2"]),
        p(
            "Goal: forecast future sales using past sales data. EDA checks trend and seasonality. ARIMA or regression models can be used. The final output may be a Power BI dashboard showing forecast, demand and inventory decisions.",
            st["body"],
        ),
        p("6. Case Study 3: Sentiment Analysis", st["h2"]),
        p(
            "Goal: classify customer reviews as positive, negative or neutral. Text preprocessing removes punctuation and stopwords. A machine learning or deep learning model predicts sentiment, and results help improve products and services.",
            st["body"],
        ),
        p("Exam Tip", st["h2"]),
        p(
            "For theory answers, write definition, diagram/table, explanation and example. For tools, always mention purpose, features and applications.",
            st["body"],
        ),
    ]
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
        title="Data Science 5 Unit Notes",
        author="Rahul yadav",
    )

    story = [
        Spacer(1, 80),
        p("Data Science", st["title"]),
        p("5 Unit Semester Exam Notes", st["title"]),
        p("Theory, tables, diagrams and exam-focused explanations<br/>Watermark: Rahul yadav", st["subtitle"]),
        make_table(
            [
                ["Unit", "Coverage"],
                ["Unit 1", "Introduction, preprocessing, EDA and descriptive statistics"],
                ["Unit 2", "Python, NumPy, Pandas, Scikit-learn and machine learning"],
                ["Unit 3", "Deep learning, PyTorch, TensorFlow, CNN and time series"],
                ["Unit 4", "R, RStudio, data structures, visualization and modeling"],
                ["Unit 5", "Analytics tools, version control and case studies"],
            ],
            [1.0 * inch, 5.0 * inch],
        ),
        PageBreak(),
    ]

    units = [unit_1(st), unit_2(st), unit_3(st), unit_4(st), unit_5(st)]
    for i, unit_story in enumerate(units):
        story.extend(unit_story)
        if i != len(units) - 1:
            story.append(PageBreak())

    story.append(PageBreak())
    story += [
        p("Important Exam Questions", st["unit"]),
        p("Unit 1", st["h2"]),
    ]
    story += bullets(
        [
            "Explain the evolution of Data Science.",
            "Describe stages of a Data Science project with diagram.",
            "Explain data preprocessing techniques with examples.",
            "Define mean, standard deviation, skewness and kurtosis.",
            "Explain box plot, pivot table and heat map.",
        ],
        st["bullet"],
    )
    story += [p("Unit 2", st["h2"])]
    story += bullets(
        [
            "Explain NumPy, Pandas and Scikit-learn.",
            "Differentiate regression and classification.",
            "Explain OLS regression and logistic regression.",
            "What are ensemble methods? Explain bagging and boosting.",
            "Explain evolutionary optimization technique.",
        ],
        st["bullet"],
    )
    story += [p("Unit 3", st["h2"])]
    story += bullets(
        [
            "Compare TensorFlow, Keras and PyTorch.",
            "Explain CNN architecture with diagram.",
            "Write short note on style transfer and sentiment analysis.",
            "Explain ARMA and ARIMA models.",
            "Explain Fourier analysis and state-space models.",
        ],
        st["bullet"],
    )
    story += [p("Unit 4", st["h2"])]
    story += bullets(
        [
            "Explain R data structures with examples.",
            "How do you import and visualize data in R?",
            "Explain regression and classification in R.",
            "Compare Python and R for Data Science.",
        ],
        st["bullet"],
    )
    story += [p("Unit 5", st["h2"])]
    story += bullets(
        [
            "Compare Weka, Orange and RapidMiner.",
            "Explain Power BI and Google Colab.",
            "Explain version control in Data Science projects.",
            "Write any two Data Science case studies.",
        ],
        st["bullet"],
    )

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
