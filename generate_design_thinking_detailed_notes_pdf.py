from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

from generate_data_science_notes_pdf import FlowChart, WatermarkDocTemplate, bullets, make_table, p, styles
from reportlab.platypus import PageBreak, Spacer


OUTPUT = "Design_Thinking_5_Unit_Detailed_Notes_Rahul_Yadav.pdf"


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
    story = [p("UNIT 1: Basics and Models of Design Thinking", st["unit"])]
    story += long_answer(
        "1. What is Different About Design Thinking?",
        [
            "Design Thinking is a human-centered approach to problem solving. It focuses on understanding users deeply, redefining problems and creating innovative solutions through ideation, prototyping and testing. It is different from traditional problem solving because it starts with user needs instead of directly starting with technology or business goals.",
            "In traditional engineering, a problem is often treated as fixed and the solution is optimized logically. In Design Thinking, the problem itself may be unclear in the beginning. Designers observe users, ask questions, understand emotions and then frame the real problem. This makes it useful for complex and uncertain problems.",
        ],
        [
            "It is user-centered and empathy-driven.",
            "It encourages creativity and experimentation.",
            "It accepts failure as part of learning.",
            "It uses prototypes to test ideas early.",
            "It combines desirability, feasibility and viability.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Point", "Traditional Approach", "Design Thinking Approach"],
                ["Starting Point", "Problem statement is fixed", "Problem is explored through users"],
                ["Focus", "Efficiency and correctness", "User value and innovation"],
                ["Method", "Linear planning", "Iterative exploration"],
                ["Testing", "Usually later stage", "Early and repeated testing"],
                ["Failure", "Avoided", "Used as learning"],
            ],
            [1.2 * inch, 2.4 * inch, 2.4 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "2. Design Thinking Skills and Principles",
        [
            "Design Thinking needs both creative and analytical skills. A good design thinker observes carefully, listens actively, asks open-ended questions and converts insights into useful solutions. Collaboration is also important because complex problems require multiple viewpoints.",
            "The principles of Design Thinking include empathy, experimentation, collaboration, visualization, iteration and action. The process does not depend only on theory; it requires practice through cases, projects and prototypes.",
        ],
        [
            "Empathy: understand user feelings, pains and needs.",
            "Observation: watch real user behavior instead of assuming.",
            "Ideation: generate many possible solutions.",
            "Collaboration: combine knowledge from different disciplines.",
            "Prototyping: make quick models to test ideas.",
            "Iteration: improve solution based on feedback.",
        ],
        st,
    )
    story += [
        p("3. Basis and Process of Design Thinking", st["h2"]),
        p("The basis of Design Thinking is that successful innovation must satisfy three conditions: desirability, feasibility and viability. Desirability means users need and value the solution. Feasibility means the solution can be built with available technology. Viability means the solution can survive as a business or practical system.", st["body"]),
        FlowChart(["Empathize", "Define", "Ideate", "Prototype", "Test", "Iterate"]),
        Spacer(1, 8),
        make_table(
            [
                ["Stage", "Meaning", "Output"],
                ["Empathize", "Understand users and context", "User insights"],
                ["Define", "Frame real problem", "Problem statement"],
                ["Ideate", "Generate solution ideas", "Idea list"],
                ["Prototype", "Build simple model", "Prototype"],
                ["Test", "Collect feedback", "Improvement points"],
            ],
            [1.2 * inch, 2.6 * inch, 2.2 * inch],
        ),
    ]
    story += long_answer(
        "4. Tools, Projects, Case Study and Models",
        [
            "Design Thinking uses tools such as empathy maps, journey maps, mind maps, affinity diagrams, brainstorming and prototypes. These tools help teams convert observations into insights and insights into solutions.",
            "Common models include Stanford d.school model, Double Diamond model and IDEO human-centered design model. In project work, students can apply these models to problems such as improving college canteen service, designing a student attendance app or creating a better library experience.",
        ],
        [
            "Stanford model: Empathize, Define, Ideate, Prototype, Test.",
            "Double Diamond: Discover, Define, Develop, Deliver.",
            "IDEO model: Hear, Create, Deliver.",
            "Case study approach helps understand real users and constraints.",
        ],
        st,
    )
    return story


def unit2(st):
    story = [p("UNIT 2: Empathy, Analysis and Ideation", st["unit"])]
    story += long_answer(
        "1. Listening and Empathizing Techniques",
        [
            "Empathy is the ability to understand the user's emotions, needs, motivations and difficulties. Listening and empathizing are important because users may not directly explain the real problem. Sometimes the designer must observe behavior, body language and context.",
            "Active listening means giving full attention, avoiding interruption, asking follow-up questions and confirming understanding. Empathy helps designers avoid assumptions and create solutions that are meaningful for real users.",
        ],
        [
            "Listen without judging the user.",
            "Ask open-ended questions beginning with what, why and how.",
            "Observe user actions in real context.",
            "Note user pain points, workarounds and emotions.",
            "Use interviews, field visits and shadowing.",
        ],
        st,
    )
    story += [
        p("2. Observation and Structured Open-Ended Approach", st["h2"]),
        p("Observation is the process of watching users perform activities in their natural environment. It reveals actual behavior rather than ideal answers. A structured open-ended approach uses planned themes but allows users to explain freely.", st["body"]),
        make_table(
            [
                ["Technique", "Purpose", "Example Question"],
                ["Observation", "Understand real behavior", "How does user actually complete the task?"],
                ["Interview", "Understand experience and opinion", "What is difficult in this process?"],
                ["Shadowing", "Follow user during task", "Observe steps in real environment"],
                ["Open-ended Question", "Get detailed answers", "How do you feel while using this service?"],
                ["Why Laddering", "Find root cause", "Why is this problem important to you?"],
            ],
            [1.4 * inch, 2.2 * inch, 2.4 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. Analysis and Design Thinking Frameworks",
        [
            "After collecting user data, the next step is analysis. Analysis means identifying patterns, grouping similar observations and finding user needs. Raw interview notes are not enough; they must be converted into insights.",
            "Frameworks help teams analyze data systematically. Examples include empathy map, persona, customer journey map, affinity diagram and problem statement framework. These tools help convert confusing data into clear design direction.",
        ],
        [
            "Affinity diagram groups similar observations.",
            "Persona represents a typical user.",
            "Problem statement defines user, need and insight.",
            "Journey map shows user experience over time.",
            "How Might We questions convert problems into opportunities.",
        ],
        st,
    )
    story += [
        FlowChart(["Interview Notes", "Group Patterns", "Find User Needs", "Create Insights", "Define Problem", "Ideate"]),
        Spacer(1, 8),
    ]
    story += long_answer(
        "4. Ideation Tools and Overcoming Cognitive Fixedness",
        [
            "Ideation is the process of generating many possible ideas. In this stage, quantity is important before quality. The goal is to explore multiple directions before selecting the best solution.",
            "Cognitive fixedness means being stuck in old ways of thinking. It stops creativity because people assume that an object or process can be used only in its usual way. Brainstorming, SCAMPER, innovation heuristics and analogies help overcome fixedness.",
        ],
        [
            "Brainstorming: generate many ideas without criticism.",
            "SCAMPER: Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, Reverse.",
            "Innovation heuristics: use prompts to create new solution directions.",
            "Behavior models: understand user motivation, ability and triggers.",
            "Case discussions help apply ideation to real problems.",
        ],
        st,
    )
    return story


def unit3(st):
    story = [p("UNIT 3: Diagrams, Maps and Research in Design Thinking", st["unit"])]
    story += long_answer(
        "1. Use of Diagrams and Maps",
        [
            "Diagrams and maps are visual tools used to organize information, understand relationships and communicate ideas. In Design Thinking, visuals are important because they make complex user experiences easy to understand.",
            "Maps also help teams reach a shared understanding. When team members see user pain points, emotions and steps visually, they can discuss the problem more effectively and generate better solutions.",
        ],
        [
            "They simplify complex information.",
            "They help identify patterns and gaps.",
            "They improve communication inside teams.",
            "They support ideation and decision making.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Tool", "Meaning", "Use"],
                ["Empathy Map", "Visualizes what user says, thinks, does and feels", "Understand user mindset"],
                ["Affinity Diagram", "Groups similar ideas or observations", "Find patterns in research data"],
                ["Mind Map", "Shows connected ideas from a central topic", "Explore idea relationships"],
                ["Journey Map", "Shows user steps, emotions and touchpoints", "Improve user experience"],
            ],
            [1.4 * inch, 2.7 * inch, 1.9 * inch],
        ),
        Spacer(1, 8),
        p("2. Empathy Map Structure", st["h2"]),
        make_table(
            [
                ["Says", "Thinks"],
                ["Direct user quotes and spoken problems.", "Hidden beliefs, worries and expectations."],
                ["Does", "Feels"],
                ["Actions and behavior observed.", "Emotions such as frustration, trust, confusion or excitement."],
            ],
            [3.0 * inch, 3.0 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. Combining Ideas into Complex Innovation Concepts",
        [
            "After ideation, ideas can be combined to create stronger innovation concepts. One idea may solve usability, another may solve cost and another may improve emotional experience. Combining them can create a more complete solution.",
            "Designers should check whether the combined concept is desirable, feasible and viable. A concept statement should explain the user, problem, solution and expected value.",
        ],
        [
            "Group related ideas.",
            "Select promising features from multiple ideas.",
            "Create concept sketches or storyboards.",
            "Check feasibility and user value.",
            "Convert concept into prototype.",
        ],
        st,
    )
    story += long_answer(
        "4. Secondary Research, Primary Research and Contextual Inquiry",
        [
            "Secondary research uses existing information such as books, reports, websites, articles and previous studies. It is useful in the beginning to understand background, market and existing solutions.",
            "Primary research collects new data directly from users through interviews, surveys, observation and field visits. Contextual inquiry is a primary research method where the researcher observes and asks questions while the user performs real tasks in the actual environment.",
        ],
        [
            "Secondary research is fast and low cost but may not be specific.",
            "Primary research gives direct user insight but takes more time.",
            "Contextual inquiry reveals real behavior and hidden problems.",
            "Both research types should be combined for better understanding.",
        ],
        st,
    )
    story += [
        FlowChart(["Secondary Research", "Primary Research", "Contextual Inquiry", "Insights", "Design Opportunities"]),
    ]
    return story


def unit4(st):
    story = [p("UNIT 4: Storytelling, Prototyping and Innovation Culture", st["unit"])]
    story += long_answer(
        "1. Storytelling in Design Thinking",
        [
            "Storytelling is the process of presenting user problems and solutions in a clear and emotional way. It helps teams, stakeholders and customers understand why a design is needed and how it creates value.",
            "A good design story includes user background, pain point, situation, proposed solution and impact. Storytelling is powerful because people remember stories better than raw data.",
        ],
        [
            "Explains user problem in relatable form.",
            "Builds emotional connection with stakeholders.",
            "Communicates design concept clearly.",
            "Helps in pitching and decision making.",
        ],
        st,
    )
    story += long_answer(
        "2. Improvisation, Scenario Planning and Development of Scenarios",
        [
            "Improvisation means creating or adapting ideas spontaneously. It helps teams explore unexpected situations and user behavior. Scenario planning is the process of imagining possible future situations and designing responses for them.",
            "A scenario describes how a user will interact with a solution in a particular context. It includes user goal, environment, steps, obstacles and outcome. Scenarios are used to test whether the solution fits real life.",
        ],
        [
            "Improvisation improves creativity and flexibility.",
            "Scenario planning prepares for different future conditions.",
            "Scenarios make abstract ideas concrete.",
            "They help evaluate user journey and usability.",
        ],
        st,
    )
    story += [
        FlowChart(["User Persona", "Goal", "Situation", "Actions", "Pain Points", "Solution Response", "Outcome"]),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. Evaluation Tools, Frog Design and Prototyping",
        [
            "Evaluation tools help test whether a design is useful, usable and acceptable. Common tools include feedback forms, usability testing, heuristic evaluation, A/B testing and observation. Frog Design is known for human-centered innovation and experience design practices.",
            "Prototyping converts ideas into tangible forms. Soft prototypes are rough and quick, such as sketches or paper models. Medium prototypes are more interactive, such as wireframes. Final prototypes are close to the real product and used for detailed testing.",
        ],
        [
            "Soft prototype: sketch, paper model, storyboard.",
            "Medium prototype: clickable wireframe, mockup, simple working model.",
            "Final prototype: high-fidelity model close to final solution.",
            "Testing prototypes reduces risk before full development.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Prototype Type", "Fidelity", "Purpose"],
                ["Soft", "Low", "Explore rough idea quickly"],
                ["Medium", "Medium", "Test flow and interaction"],
                ["Final", "High", "Validate near-final design"],
            ],
            [1.6 * inch, 1.4 * inch, 3.0 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "4. Communication, Innovation Culture and Usability Studies",
        [
            "Design frameworks strengthen communication by giving teams a shared language and process. Visuals, stories, prototypes and user evidence help convince stakeholders and reduce misunderstandings.",
            "A culture of innovation is sustained by encouraging experimentation, accepting failure, supporting collaboration and rewarding creative problem solving. Usability studies test whether users can use the solution effectively, efficiently and satisfactorily.",
        ],
        [
            "Usability studies observe real users using the product.",
            "Metrics include task success, time taken, errors and satisfaction.",
            "Innovation culture needs leadership support and psychological safety.",
            "Communication should be clear, visual and user-centered.",
        ],
        st,
    )
    return story


def unit5(st):
    story = [p("UNIT 5: Engineering Design and Entrepreneurship", st["unit"])]
    story += long_answer(
        "1. Engineering Aspect of Design",
        [
            "Engineering design converts user needs into practical and reliable products or systems. A design should not only be attractive but also technically feasible, safe, reliable and cost-effective.",
            "Engineering aspects include electrical design, mechanical design, material selection, safety, reliability, manufacturability and maintenance. A good solution balances user need, technical constraints and business goals.",
        ],
        [
            "Electrical aspect: circuits, power, sensors and control.",
            "Mechanical aspect: structure, movement, strength and ergonomics.",
            "Material aspect: durability, weight, cost and sustainability.",
            "Safety aspect: risk reduction and user protection.",
            "Reliability aspect: consistent performance over time.",
        ],
        st,
    )
    story += [
        make_table(
            [
                ["Aspect", "Design Consideration", "Example"],
                ["Electrical", "Voltage, current, sensors, wiring", "Smart attendance device"],
                ["Mechanical", "Shape, strength, movement", "Adjustable chair"],
                ["Material", "Cost, durability, sustainability", "Reusable bottle material"],
                ["Safety", "Hazard prevention", "Insulation, emergency stop"],
                ["Reliability", "Long-term performance", "Testing under repeated use"],
            ],
            [1.2 * inch, 2.7 * inch, 2.1 * inch],
        ),
        Spacer(1, 8),
    ]
    story += long_answer(
        "2. Creating Business Model",
        [
            "A business model explains how an idea creates, delivers and captures value. Even a technically strong idea may fail if it has no clear users, revenue source or cost structure.",
            "The Business Model Canvas is a common tool used to design business models. It includes customer segments, value proposition, channels, customer relationships, revenue streams, key resources, key activities, partners and cost structure.",
        ],
        [
            "Value proposition explains why customers need the product.",
            "Customer segment defines target users.",
            "Revenue stream explains how money will be earned.",
            "Cost structure identifies major expenses.",
            "Channels describe how product reaches customers.",
        ],
        st,
    )
    story += [
        FlowChart(["User Problem", "Value Proposition", "Target Customer", "Revenue Model", "Cost Structure", "Launch Plan"]),
        Spacer(1, 8),
    ]
    story += long_answer(
        "3. Entrepreneurship and Startup Fundamentals",
        [
            "Entrepreneurship is the process of identifying opportunities, creating innovative solutions and building a business around them. An entrepreneur takes risk, organizes resources and creates value for customers and society.",
            "A startup is a young business designed to search for a scalable and repeatable business model. Startups usually begin with uncertainty, limited resources and high learning needs. Design Thinking helps startups understand customers and validate ideas early.",
        ],
        [
            "Entrepreneur identifies a problem or opportunity.",
            "Startup begins with idea validation and minimum viable product.",
            "Customer feedback is used to improve product.",
            "Business model must be tested and refined.",
            "Successful startups solve real problems at scalable level.",
        ],
        st,
    )
    story += long_answer(
        "4. Challenges, Possibilities and How to Start Up",
        [
            "Entrepreneurship has challenges such as funding, market competition, customer acquisition, product development, legal compliance and team building. However, it also provides possibilities such as innovation, employment generation, social impact and financial growth.",
            "To start up, an entrepreneur should identify a problem, research users, create a value proposition, build a prototype or MVP, test with customers, prepare business model, arrange resources and launch gradually.",
        ],
        [
            "Challenges: capital, risk, competition, uncertainty and execution.",
            "Possibilities: innovation, independence, job creation and growth.",
            "Steps: problem identification, research, MVP, validation, business model, launch.",
            "Success requires persistence, customer focus and continuous learning.",
        ],
        st,
    )
    story += [
        p("5. Being Successful as an Entrepreneur", st["h2"]),
        p("A successful entrepreneur understands customer needs, learns from failure, adapts quickly and builds a strong team. Success depends on execution, not only on idea. Entrepreneurs should communicate clearly, manage finance carefully and continuously improve the product.", st["body"]),
    ]
    return story


def exam_questions(st):
    story = [p("Important Semester Exam Questions", st["unit"])]
    data = {
        "Unit 1": [
            "What is Design Thinking? How is it different from traditional problem solving?",
            "Explain principles and skills of Design Thinking.",
            "Explain Design Thinking process with diagram.",
            "Explain models of Design Thinking.",
        ],
        "Unit 2": [
            "Explain listening and empathizing techniques.",
            "What is structured open-ended approach?",
            "Explain ideation tools and brainstorming.",
            "What is cognitive fixedness? How can it be overcome?",
        ],
        "Unit 3": [
            "Explain empathy map, affinity diagram, mind map and journey map.",
            "Differentiate primary and secondary research.",
            "Explain contextual inquiry.",
            "How are ideas combined into innovation concepts?",
        ],
        "Unit 4": [
            "Explain storytelling and scenario planning.",
            "Explain soft, medium and final prototypes.",
            "Explain usability studies.",
            "How can a culture of innovation be sustained?",
        ],
        "Unit 5": [
            "Explain engineering aspects of design.",
            "Explain safety and reliability aspects.",
            "What is business model canvas?",
            "What is entrepreneurship? How to start a startup?",
            "Explain challenges and possibilities of entrepreneurship.",
        ],
    }
    for unit, qs in data.items():
        story.append(p(unit, st["h2"]))
        story += bullets(qs, st["bullet"])
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
        title="Detailed Design Thinking 5 Unit Notes",
        author="Rahul yadav",
    )
    story = [
        Spacer(1, 75),
        p("Design Thinking and Entrepreneurship", st["title"]),
        p("Detailed 5 Unit Semester Exam Notes", st["title"]),
        p("Theory, tables, diagrams, maps and exam-focused questions<br/>Watermark: Rahul yadav", st["subtitle"]),
        make_table(
            [
                ["Unit", "Main Topics"],
                ["Unit 1", "Design Thinking basics, principles, process, tools, projects and models"],
                ["Unit 2", "Listening, empathy, observation, analysis, frameworks and ideation"],
                ["Unit 3", "Empathy map, affinity diagram, mind map, journey map and research"],
                ["Unit 4", "Storytelling, scenarios, prototyping, communication and usability"],
                ["Unit 5", "Engineering design, safety, reliability, business model, startup and entrepreneurship"],
            ],
            [1.0 * inch, 5.0 * inch],
        ),
        PageBreak(),
    ]

    sections = [unit1(st), unit2(st), unit3(st), unit4(st), unit5(st), exam_questions(st)]
    for idx, section in enumerate(sections):
        story.extend(section)
        if idx != len(sections) - 1:
            story.append(PageBreak())
    doc.build(story)


if __name__ == "__main__":
    build_pdf()
