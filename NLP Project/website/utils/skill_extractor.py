import re

# ============================================================
# SKILL TAXONOMY
# One skill belongs to one category only.
# ============================================================

SKILL_TAXONOMY = {
    "Programming": [
        "Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript",
        "R", "Go", "Rust", "PHP", "Ruby", "Kotlin", "Swift", "Scala",
        "MATLAB", "Dart", "Objective-C", "Perl", "Bash", "PowerShell"
    ],

    "Database": [
        "SQL", "MySQL", "PostgreSQL", "Oracle", "SQL Server", "SQLite",
        "MongoDB", "Cassandra", "Redis", "Firebase", "DynamoDB", "MariaDB",
        "Neo4j", "PL/SQL", "Database Design", "Database Management",
        "Database Administration", "Stored Procedures"
    ],

    "Data Libraries": [
        "Pandas", "NumPy", "Polars", "SciPy", "Statsmodels"
    ],

    "Data Visualization": [
        "Matplotlib", "Seaborn", "Plotly", "Bokeh", "Altair"
    ],

    "BI Tools": [
        "Power BI", "Tableau", "Qlik Sense", "Looker", "Looker Studio",
        "MicroStrategy", "Domo"
    ],

    "Spreadsheet Tools": [
        "Excel", "Google Sheets"
    ],

    "Machine Learning": [
        "Scikit-learn", "XGBoost", "LightGBM", "CatBoost", "Random Forest",
        "Linear Regression", "Logistic Regression", "Decision Tree", "KNN",
        "SVM", "Naive Bayes", "Clustering", "K-Means", "PCA",
        "Machine Learning", "Feature Engineering", "Model Evaluation"
    ],

    "Deep Learning": [
        "TensorFlow", "PyTorch", "Keras", "OpenCV", "CNN", "RNN", "LSTM",
        "GRU", "GAN", "Transformer", "Neural Networks", "Deep Learning",
        "Computer Vision"
    ],

    "NLP": [
        "NLP", "Natural Language Processing", "NLTK", "spaCy", "BERT",
        "DistilBERT", "Transformers", "Word2Vec", "TF-IDF", "GloVe",
        "Text Classification", "Named Entity Recognition",
        "Sentiment Analysis", "Tokenization", "Text Preprocessing",
        "Large Language Models", "LLM", "Generative AI", "Prompt Engineering"
    ],

    "Web Development": [
        "HTML", "CSS", "React", "Angular", "Vue", "Django", "Flask",
        "FastAPI", "REST API", "Node.js", "Express.js", "Spring Boot",
        "ASP.NET", "Laravel", "Next.js", "Bootstrap", "Redux", "GraphQL",
        "Microservices"
    ],

    "Cloud": [
        "AWS", "Azure", "GCP", "Google Cloud", "Amazon Web Services",
        "Microsoft Azure", "EC2", "S3", "Lambda", "RDS", "CloudFormation",
        "Cloud Computing", "Cloud Architecture"
    ],

    "DevOps": [
        "Docker", "Kubernetes", "Git", "GitHub", "Jenkins", "Terraform",
        "CI/CD", "Linux", "Ansible", "GitLab", "Maven", "Nginx",
        "Prometheus", "Grafana"
    ],

    "Big Data": [
        "Hadoop", "Apache Spark", "Spark", "PySpark", "Hive", "Kafka",
        "Airflow", "Databricks", "Flink", "HBase", "Snowflake",
        "Data Warehousing", "ETL", "Data Pipelines"
    ],

    "Testing": [
        "Software Testing", "Manual Testing", "Automation Testing",
        "Selenium", "API Testing", "JMeter", "Load Testing", "Stress Testing",
        "Regression Testing", "Functional Testing", "Test Cases",
        "Bug Tracking", "TestNG", "JUnit", "Cypress", "Playwright", "Postman"
    ],

    "Cybersecurity": [
        "Cybersecurity", "Network Security", "Cloud Security", "SIEM",
        "Firewalls", "Ethical Hacking", "Penetration Testing",
        "Threat Detection", "Incident Response", "Kali Linux", "Burp Suite",
        "Metasploit", "Nmap", "Vulnerability Assessment", "Security Auditing",
        "IAM", "Cryptography"
    ],

    "Mobile Development": [
        "Android", "Android SDK", "Android Studio", "iOS", "iOS SDK", "Xcode",
        "Flutter", "React Native", "Firebase", "Jetpack Compose", "SwiftUI"
    ],

    "Design": [
        "UI Design", "UX Design", "Product Design", "Graphic Design", "Figma",
        "Adobe XD", "Photoshop", "Illustrator", "Canva", "Wireframing",
        "Prototyping", "User Research", "Usability Testing", "Typography",
        "Blender", "3D Modeling"
    ],

    "Project Management": [
        "Project Management", "Product Management", "Agile", "Scrum", "JIRA",
        "Risk Management", "Sprint Planning", "Roadmap", "Product Strategy",
        "Requirements Gathering", "Business Analysis", "Stakeholder Management"
    ],

    "Networking": [
        "Networking", "TCP/IP", "Routing", "Switching", "Cisco", "DNS",
        "DHCP", "VPN", "LAN", "WAN", "Network Administration"
    ],

    "Other Technical": [
        "Blockchain", "Ethereum", "Smart Contracts", "Web3", "IoT",
        "Embedded Systems", "Arduino", "Raspberry Pi", "Unity",
        "Unreal Engine", "Game Development", "Salesforce", "CRM", "SAP",
        "ERP", "ABAP", "Business Processes", "Windows", "Active Directory",
        "Troubleshooting", "Backup"
    ],

    "Development Tools": [
        "Visual Studio Code", "IntelliJ IDEA", "Eclipse", "GitHub Actions",
        "Bitbucket"
    ],

    "Soft Skills": [
        "Communication", "Teamwork", "Leadership", "Problem Solving",
        "Critical Thinking", "Analytical Thinking", "Time Management",
        "Adaptability", "Creativity", "Collaboration", "Decision Making",
        "Attention to Detail", "Interpersonal Skills", "Presentation Skills",
        "Negotiation", "Conflict Resolution", "Stakeholder Management",
        "Work Ethic", "Emotional Intelligence", "Organization", "Multitasking",
        "Self Motivation", "Learning Agility", "Customer Service", "Mentoring",
        "Team Leadership", "Written Communication", "Verbal Communication"
    ]
}

# ============================================================
# 100 JOB ROLES
# ============================================================

ROLE_SKILLS = {
    "Data Analyst": ["Python","SQL","Pandas","NumPy","Excel","Power BI","Tableau","Statistics","Data Analysis","Data Visualization"],
    "Data Scientist": ["Python","SQL","Pandas","NumPy","Scikit-learn","TensorFlow","PyTorch","Machine Learning","Deep Learning","Statistics"],
    "Machine Learning Engineer": ["Python","SQL","NumPy","Pandas","Scikit-learn","TensorFlow","PyTorch","Machine Learning","Deep Learning","Feature Engineering","Model Evaluation"],
    "AI Engineer": ["Python","Machine Learning","Deep Learning","TensorFlow","PyTorch","Scikit-learn","NLP","Computer Vision","Generative AI"],
    "NLP Engineer": ["Python","NLP","NLTK","spaCy","BERT","Transformers","TF-IDF","Scikit-learn","Text Classification","Named Entity Recognition"],
    "Deep Learning Engineer": ["Python","TensorFlow","PyTorch","Keras","CNN","RNN","LSTM","Neural Networks","Deep Learning"],
    "Generative AI Engineer": ["Python","Generative AI","LLM","Large Language Models","Transformers","Prompt Engineering","NLP","PyTorch"],
    "Data Engineer": ["Python","SQL","Pandas","Apache Spark","PySpark","Hadoop","Kafka","Airflow","Databricks","Data Pipelines","ETL"],
    "Big Data Engineer": ["Python","SQL","Hadoop","Apache Spark","PySpark","Hive","Kafka","Databricks","ETL"],
    "Data Architect": ["SQL","PostgreSQL","Database Design","Data Warehousing","AWS","Azure","GCP"],
    "Business Analyst": ["Excel","SQL","Power BI","Tableau","Business Analysis","Requirements Gathering","Data Analysis","Communication"],
    "Business Intelligence Developer": ["SQL","Power BI","Tableau","Excel","Data Visualization","Data Warehousing","ETL"],
    "Database Administrator": ["SQL","MySQL","PostgreSQL","Oracle","SQL Server","Database Administration","Database Management","Backup"],
    "Database Developer": ["SQL","MySQL","PostgreSQL","Oracle","Database Design","Stored Procedures","PL/SQL"],
    "SQL Developer": ["SQL","MySQL","PostgreSQL","Oracle","SQL Server","Stored Procedures","Database Design"],
    "Software Developer": ["Python","Java","C++","JavaScript","SQL","Git"],
    "Software Engineer": ["Python","Java","C++","JavaScript","SQL","Git"],
    "Full Stack Developer": ["HTML","CSS","JavaScript","React","Node.js","Express.js","REST API","SQL","MongoDB","Git"],
    "Frontend Developer": ["HTML","CSS","JavaScript","React","Angular","Vue","Redux","Git"],
    "Backend Developer": ["Python","Java","Node.js","Express.js","REST API","SQL","MongoDB","Git"],
    "Java Developer": ["Java","Spring Boot","SQL","REST API","Git","Maven"],
    "Python Developer": ["Python","Django","Flask","FastAPI","SQL","REST API","Git"],
    "JavaScript Developer": ["JavaScript","TypeScript","HTML","CSS","React","Node.js","Git"],
    "TypeScript Developer": ["TypeScript","JavaScript","React","Node.js","HTML","CSS","Git"],
    "React Developer": ["React","JavaScript","HTML","CSS","Redux","REST API","Git"],
    "Angular Developer": ["Angular","TypeScript","JavaScript","HTML","CSS","REST API","Git"],
    "Vue Developer": ["Vue","JavaScript","TypeScript","HTML","CSS","REST API","Git"],
    "Node.js Developer": ["Node.js","JavaScript","Express.js","REST API","MongoDB","SQL","Git"],
    "PHP Developer": ["PHP","Laravel","MySQL","HTML","CSS","JavaScript","Git"],
    ".NET Developer": ["C#","ASP.NET","SQL Server","REST API","Git","Azure"],
    "C++ Developer": ["C++","C","Git"],
    "C Developer": ["C","C++","Linux","Git"],
    "Go Developer": ["Go","REST API","Microservices","Docker","Kubernetes","Git"],
    "Rust Developer": ["Rust","C++","Linux","Git","Docker"],
    "DevOps Engineer": ["Linux","Docker","Kubernetes","Jenkins","Git","GitHub","Terraform","CI/CD"],
    "Cloud Engineer": ["AWS","Azure","GCP","Docker","Kubernetes","Linux","Terraform"],
    "AWS Engineer": ["AWS","EC2","S3","Lambda","RDS","CloudFormation","Docker","Linux"],
    "Azure Engineer": ["Azure","Cloud Computing","Docker","Kubernetes","Linux"],
    "GCP Engineer": ["GCP","Google Cloud","Kubernetes","Docker","Cloud Computing","Linux"],
    "Cloud Architect": ["AWS","Azure","GCP","Cloud Architecture","Cloud Computing","Kubernetes","Terraform"],
    "Solutions Architect": ["AWS","Azure","GCP","Cloud Architecture","Microservices","REST API","Database Design"],
    "Site Reliability Engineer": ["Linux","Docker","Kubernetes","Git","CI/CD","Prometheus","Grafana","AWS"],
    "Platform Engineer": ["Linux","Docker","Kubernetes","Terraform","GitHub Actions","CI/CD","AWS"],
    "Cyber Security Analyst": ["Cybersecurity","SIEM","Network Security","Firewalls","Threat Detection","Incident Response","Linux"],
    "Cyber Security Engineer": ["Cybersecurity","Network Security","Cloud Security","SIEM","Firewalls","IAM","Linux"],
    "Ethical Hacker": ["Ethical Hacking","Penetration Testing","Kali Linux","Burp Suite","Metasploit","Nmap"],
    "Penetration Tester": ["Penetration Testing","Ethical Hacking","Kali Linux","Burp Suite","Metasploit","Nmap"],
    "SOC Analyst": ["SIEM","Cybersecurity","Threat Detection","Incident Response","Network Security","Linux"],
    "Security Engineer": ["Cybersecurity","Network Security","Cloud Security","Firewalls","SIEM","IAM","Cryptography"],
    "Network Engineer": ["Networking","TCP/IP","Routing","Switching","Cisco","DNS","DHCP","VPN"],
    "Network Administrator": ["Networking","TCP/IP","Cisco","DNS","DHCP","VPN","Network Administration"],
    "System Administrator": ["Linux","Windows","Networking","Active Directory","System Administration","PowerShell","Bash"],
    "Linux Administrator": ["Linux","Bash","Networking","Docker","System Administration"],
    "Technical Support Engineer": ["Technical Support","Networking","Linux","Windows","Troubleshooting","Customer Service"],
    "IT Support Specialist": ["Technical Support","Windows","Linux","Networking","Troubleshooting","Customer Service"],
    "QA Engineer": ["Software Testing","Manual Testing","Automation Testing","Selenium","API Testing","Test Cases","JIRA"],
    "Software Tester": ["Software Testing","Manual Testing","Test Cases","Bug Tracking","JIRA","API Testing"],
    "Automation Tester": ["Automation Testing","Selenium","Java","Python","TestNG","API Testing","Jenkins"],
    "Manual Tester": ["Manual Testing","Test Cases","Bug Tracking","JIRA","Regression Testing","Functional Testing"],
    "Performance Tester": ["Performance Testing","JMeter","Load Testing","Stress Testing"],
    "Mobile App Developer": ["Flutter","React Native","Android","iOS","Firebase","Git"],
    "Android Developer": ["Java","Kotlin","Android SDK","Android Studio","Firebase","Git"],
    "iOS Developer": ["Swift","Objective-C","iOS","iOS SDK","Xcode","SwiftUI","Git"],
    "Flutter Developer": ["Dart","Flutter","Firebase","Android","iOS","Git"],
    "React Native Developer": ["JavaScript","TypeScript","React Native","Android","iOS","Firebase","Git"],
    "UI UX Designer": ["UI Design","UX Design","Figma","Wireframing","Prototyping","User Research"],
    "UI Designer": ["UI Design","Figma","Adobe XD","Photoshop","Wireframing","Prototyping"],
    "UX Designer": ["UX Design","Figma","User Research","Wireframing","Prototyping","Usability Testing"],
    "Product Designer": ["Product Design","UI Design","UX Design","Figma","Prototyping","User Research"],
    "Graphic Designer": ["Graphic Design","Photoshop","Illustrator","Figma","Canva","Typography"],
    "Product Manager": ["Product Management","Product Strategy","Roadmap","Agile","Market Research","Stakeholder Management"],
    "Project Manager": ["Project Management","Agile","JIRA","Risk Management","Stakeholder Management","Communication"],
    "Scrum Master": ["Scrum","Agile","JIRA","Sprint Planning","Leadership","Communication"],
    "Blockchain Developer": ["Blockchain","Solidity","Ethereum","Smart Contracts","Web3","JavaScript"],
    "Web3 Developer": ["Web3","Blockchain","Solidity","Ethereum","Smart Contracts","JavaScript"],
    "IoT Engineer": ["IoT","Python","C++","Arduino","Raspberry Pi","Embedded Systems"],
    "Embedded Engineer": ["Embedded Systems","C","C++","Arduino","Raspberry Pi","Linux"],
    "Game Developer": ["Unity","Unreal Engine","C#","C++","Game Development","3D Modeling","Blender"],
    "Salesforce Developer": ["Salesforce","CRM","JavaScript","REST API","Git"],
    "SAP Developer": ["SAP","ABAP","ERP","SQL","Business Processes"],
    "ERP Consultant": ["ERP","SAP","Business Processes","SQL","Project Management"],
    "IT Consultant": ["Cloud Computing","Business Analysis","Project Management","Communication","Problem Solving"],
    "Data Visualization Specialist": ["Python","Pandas","NumPy","Matplotlib","Seaborn","Plotly","Power BI","Tableau"],
    "Statistician": ["R","Python","Statistics","Pandas","NumPy","SciPy","Statsmodels","Excel"],
    "Research Scientist": ["Python","R","Statistics","Machine Learning","Deep Learning","TensorFlow","PyTorch"],
    "Computer Vision Engineer": ["Python","OpenCV","TensorFlow","PyTorch","CNN","Computer Vision","Deep Learning"],
    "MLOps Engineer": ["Python","Machine Learning","Docker","Kubernetes","CI/CD","AWS"],
    "AI Research Scientist": ["Python","Machine Learning","Deep Learning","PyTorch","TensorFlow","NLP","Computer Vision"],
    "Data Quality Analyst": ["SQL","Excel","Python","Pandas","Data Cleaning","Data Analysis","Statistics"],
    "ETL Developer": ["SQL","Python","ETL","Data Pipelines","Apache Spark","Airflow","Data Warehousing"],
    "Data Warehouse Developer": ["SQL","Data Warehousing","ETL","Snowflake","Apache Spark","Data Pipelines"],
    "Analytics Engineer": ["SQL","Python","Pandas","Data Warehousing","ETL"],
    "Reporting Analyst": ["Excel","SQL","Power BI","Tableau","Reporting","Data Visualization"],
    "Financial Analyst": ["Excel","SQL","Power BI","Tableau","Statistics","Data Analysis"],
    "Marketing Analyst": ["Excel","SQL","Power BI","Tableau","Data Analysis","Statistics"],
    "Operations Analyst": ["Excel","SQL","Power BI","Tableau","Data Analysis","Reporting"],
    "Product Analyst": ["SQL","Python","Excel","Power BI","Tableau","Data Analysis","Statistics"],
    "IT Project Coordinator": ["Project Management","JIRA","Agile","Excel","Communication"],
    "Technical Project Manager": ["Project Management","Agile","JIRA","Cloud Computing","Communication"]
}

# Keep role skills limited to skills that exist in the taxonomy.
SKILL_CATEGORY = {}
for category, skills in SKILL_TAXONOMY.items():
    for skill in skills:
        if skill not in SKILL_CATEGORY:
            SKILL_CATEGORY[skill] = category

ALL_SKILLS = list(dict.fromkeys(
    skill for skills in SKILL_TAXONOMY.values() for skill in skills
))

# Extra terms used by role definitions.
EXTRA_SKILLS = {
    "Statistics": "Data & Analytics",
    "Data Analysis": "Data & Analytics",
    "Data Visualization": "Data Visualization",
    "Reporting": "Data & Analytics",
    "System Administration": "Other Technical",
    "Technical Support": "Other Technical",
    "Software Development": "Other Technical",
    "Market Research": "Project Management",
    "Backup": "Other Technical"
}
for skill, category in EXTRA_SKILLS.items():
    if skill not in SKILL_CATEGORY:
        SKILL_CATEGORY[skill] = category
        SKILL_TAXONOMY.setdefault(category, []).append(skill)
        ALL_SKILLS.append(skill)

SKILL_NORMALIZATION = {
    "python3": "Python",
    "python 3": "Python",
    "powerbi": "Power BI",
    "power-bi": "Power BI",
    "ms excel": "Excel",
    "microsoft excel": "Excel",
    "postgres": "PostgreSQL",
    "postgresql database": "PostgreSQL",
    "postgre sql": "PostgreSQL",
    "scikit learn": "Scikit-learn",
    "sklearn": "Scikit-learn",
    "natural language processing": "Natural Language Processing",
    "natural-language-processing": "Natural Language Processing",
    "nodejs": "Node.js",
    "node js": "Node.js",
    "ci cd": "CI/CD",
    "ci-cd": "CI/CD",
    "tf idf": "TF-IDF",
    "tf-idf": "TF-IDF",
    "amazon web services": "AWS",
    "microsoft azure": "Azure"
}

ROLE_ALIASES = {
    "data analytics": "Data Analyst",
    "data analysis": "Data Analyst",
    "data analyst": "Data Analyst",
    "data science": "Data Scientist",
    "ml engineer": "Machine Learning Engineer",
    "ai developer": "AI Engineer",
    "artificial intelligence engineer": "AI Engineer",
    "nlp developer": "NLP Engineer",
    "gen ai engineer": "Generative AI Engineer",
    "genai engineer": "Generative AI Engineer",
    "full stack dev": "Full Stack Developer",
    "fullstack developer": "Full Stack Developer",
    "full-stack developer": "Full Stack Developer",
    "full stack engineer": "Full Stack Developer",
    "frontend dev": "Frontend Developer",
    "front end developer": "Frontend Developer",
    "front end dev": "Frontend Developer",
    "frontend engineer": "Frontend Developer",
    "backend dev": "Backend Developer",
    "back end developer": "Backend Developer",
    "back end dev": "Backend Developer",
    "backend engineer": "Backend Developer",
    "software dev": "Software Developer",
    "java dev": "Java Developer",
    "python dev": "Python Developer",
    "react dev": "React Developer",
    "node developer": "Node.js Developer",
    "nodejs developer": "Node.js Developer",
    "javascript dev": "JavaScript Developer",
    "js developer": "JavaScript Developer",
    "devops": "DevOps Engineer",
    "dev ops engineer": "DevOps Engineer",
    "cloud": "Cloud Engineer",
    "aws developer": "AWS Engineer",
    "aws cloud engineer": "AWS Engineer",
    "azure developer": "Azure Engineer",
    "azure cloud engineer": "Azure Engineer",
    "gcp developer": "GCP Engineer",
    "gcp cloud engineer": "GCP Engineer",
    "sre": "Site Reliability Engineer",
    "cyber security": "Cyber Security Analyst",
    "cybersecurity analyst": "Cyber Security Analyst",
    "ethical hacking": "Ethical Hacker",
    "pentester": "Penetration Tester",
    "penetration testing": "Penetration Tester",
    "soc": "SOC Analyst",
    "soc analyst": "SOC Analyst",
    "dba": "Database Administrator",
    "database admin": "Database Administrator",
    "qa": "QA Engineer",
    "qa tester": "QA Engineer",
    "quality assurance engineer": "QA Engineer",
    "automation test engineer": "Automation Tester",
    "manual test engineer": "Manual Tester",
    "pm": "Project Manager",
    "project management": "Project Manager",
    "product management": "Product Manager",
    "ui ux designer": "UI UX Designer",
    "ui/ux designer": "UI UX Designer",
    "ui ux": "UI UX Designer",
    "ui designer": "UI Designer",
    "ux designer": "UX Designer",
    "blockchain dev": "Blockchain Developer",
    "blockchain engineer": "Blockchain Developer",
    "iot developer": "IoT Engineer",
    "embedded systems engineer": "Embedded Engineer",
    "game dev": "Game Developer",
    "networking engineer": "Network Engineer",
    "sysadmin": "System Administrator",
    "system admin": "System Administrator",
    "tech support engineer": "Technical Support Engineer",
    "technical support": "Technical Support Engineer",
    "salesforce dev": "Salesforce Developer",
    "sap dev": "SAP Developer",
    "bi developer": "Business Intelligence Developer"
}

def preprocess_text(text):
    text = str(text).lower()
    text = text.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", text).strip()

def normalize_skill(skill):
    value = str(skill).strip().lower()
    if value in SKILL_NORMALIZATION:
        return SKILL_NORMALIZATION[value]
    for standard in ALL_SKILLS:
        if standard.lower() == value:
            return standard
    return str(skill).strip().title()

def normalize_skills(skills):
    result = []
    for skill in skills:
        value = normalize_skill(skill)
        if value not in result:
            result.append(value)
    return result

def normalize_role(text):
    value = preprocess_text(text)
    if value in ROLE_ALIASES:
        return ROLE_ALIASES[value]
    for role in ROLE_SKILLS:
        if value == preprocess_text(role):
            return role
    return None

def get_skill_category(skill):
    normalized = normalize_skill(skill)
    return SKILL_CATEGORY.get(normalized, "Other Technical")

def get_categories(skill_list):
    result = []
    for skill in skill_list:
        category = get_skill_category(skill)
        if category not in result:
            result.append(category)
    return result

def dictionary_extract(text):
    text = preprocess_text(text)
    found = []
    for skill in sorted(ALL_SKILLS, key=len, reverse=True):
        pattern = r"(?<![a-z0-9])" + re.escape(skill.lower()) + r"(?![a-z0-9])"
        if re.search(pattern, text):
            found.append(skill)
    return normalize_skills(found)

def regex_matching(text):
    found = []
    for skill in sorted(ALL_SKILLS, key=len, reverse=True):
        pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])"
        if re.search(pattern, str(text), re.IGNORECASE):
            found.append(skill)
    return normalize_skills(found)

def extract_text_skills(text):
    return normalize_skills(dictionary_extract(text) + regex_matching(text))

def get_role_skills(role):
    valid = []
    for skill in ROLE_SKILLS.get(role, []):
        normalized = normalize_skill(skill)
        if normalized in SKILL_CATEGORY and normalized not in valid:
            valid.append(normalized)
    return valid

def extract_skills(text):
    """
    Job Title only -> predefined role skills.
    Full JD -> only explicitly mentioned skills.
    No semantic similarity is used, so absent skills are not invented.
    """
    if not text or not str(text).strip():
        return [], {}

    original = str(text).strip()
    role = normalize_role(original)

    if role:
        skills = get_role_skills(role)
    else:
        skills = extract_text_skills(original)

    categories = {skill: get_skill_category(skill) for skill in skills}
    return skills, categories

def extract_skills_detailed(text):
    skills, categories = extract_skills(text)
    return {
        "skills": skills,
        "categories": categories,
        "category_list": get_categories(skills)
    }
