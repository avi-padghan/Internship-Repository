import re
from functools import lru_cache

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# SKILL TAXONOMY
# ============================================================

SKILL_TAXONOMY = {

    # --------------------------------------------------------
    # Programming
    # --------------------------------------------------------

    "Programming": [
        "Python",
        "Java",
        "C",
        "C++",
        "C#",
        "JavaScript",
        "TypeScript",
        "R",
        "Go",
        "Rust",
        "PHP",
        "Ruby",
        "Kotlin",
        "Swift",
        "Scala",
        "MATLAB"
    ],


    # --------------------------------------------------------
    # Database
    # --------------------------------------------------------

    "Database": [
        "SQL",
        "MySQL",
        "PostgreSQL",
        "Oracle",
        "SQL Server",
        "SQLite",
        "MongoDB",
        "Cassandra",
        "Redis",
        "Firebase",
        "DynamoDB",
        "MariaDB",
        "Neo4j"
    ],


    # --------------------------------------------------------
    # Data Libraries
    # --------------------------------------------------------

    "Data Libraries": [
        "Pandas",
        "NumPy",
        "Polars",
        "SciPy",
        "Statsmodels"
    ],


    # --------------------------------------------------------
    # Data Visualization
    # --------------------------------------------------------

    "Data Visualization": [
        "Matplotlib",
        "Seaborn",
        "Plotly",
        "Bokeh",
        "Altair"
    ],


    # --------------------------------------------------------
    # BI Tools
    # --------------------------------------------------------

    "BI Tools": [
        "Power BI",
        "Tableau",
        "Qlik Sense",
        "Looker",
        "Looker Studio",
        "MicroStrategy",
        "Domo"
    ],


    # --------------------------------------------------------
    # Spreadsheet Tools
    # --------------------------------------------------------

    "Spreadsheet Tools": [
        "Excel",
        "Microsoft Excel",
        "Google Sheets"
    ],


    # --------------------------------------------------------
    # Machine Learning
    # --------------------------------------------------------

    "Machine Learning": [
        "Scikit-learn",
        "XGBoost",
        "LightGBM",
        "CatBoost",
        "Random Forest",
        "Linear Regression",
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "SVM",
        "Naive Bayes",
        "Clustering",
        "K-Means",
        "PCA"
    ],


    # --------------------------------------------------------
    # Deep Learning
    # --------------------------------------------------------

    "Deep Learning": [
        "TensorFlow",
        "PyTorch",
        "Keras",
        "OpenCV",
        "CNN",
        "RNN",
        "LSTM",
        "GRU",
        "GAN",
        "Transformer"
    ],


    # --------------------------------------------------------
    # NLP
    # --------------------------------------------------------

    "NLP": [
        "NLP",
        "NLTK",
        "spaCy",
        "BERT",
        "DistilBERT",
        "Transformers",
        "Word2Vec",
        "TF-IDF",
        "GloVe"
    ],


    # --------------------------------------------------------
    # Web Development
    # --------------------------------------------------------

    "Web Development": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Angular",
        "Vue",
        "Django",
        "Flask",
        "FastAPI",
        "REST API",
        "Node.js"
    ],


    # --------------------------------------------------------
    # Cloud
    # --------------------------------------------------------

    "Cloud": [
        "AWS",
        "Azure",
        "GCP",
        "Google Cloud",
        "Amazon Web Services",
        "Microsoft Azure"
    ],


    # --------------------------------------------------------
    # DevOps
    # --------------------------------------------------------

    "DevOps": [
        "Docker",
        "Kubernetes",
        "Git",
        "GitHub",
        "Jenkins",
        "Terraform",
        "CI/CD",
        "Linux"
    ],


    # --------------------------------------------------------
    # Big Data
    # --------------------------------------------------------

    "Big Data": [
        "Hadoop",
        "Apache Spark",
        "Spark",
        "PySpark",
        "Hive",
        "Kafka",
        "Airflow",
        "Databricks"
    ]
}


# ============================================================
# SKILL NORMALIZATION
# ============================================================

SKILL_NORMALIZATION = {

    # Python
    "python3": "Python",
    "python 3": "Python",
    "python programming": "Python",

    # Power BI
    "powerbi": "Power BI",
    "power-bi": "Power BI",
    "power bi": "Power BI",

    # Excel
    "ms excel": "Excel",
    "microsoft excel": "Excel",
    "excel spreadsheet": "Excel",

    # Google Sheets
    "google sheet": "Google Sheets",

    # PostgreSQL
    "postgres": "PostgreSQL",
    "postgresql database": "PostgreSQL",
    "postgre sql": "PostgreSQL",

    # Scikit-learn
    "scikit learn": "Scikit-learn",
    "sklearn": "Scikit-learn",

    # Machine Learning
    "machinelearning": "Machine Learning",
    "machine learning": "Machine Learning",

    # NLP
    "natural language processing": "NLP",
    "natural-language-processing": "NLP",

    # Artificial Intelligence
    "artificial intelligence": "AI",

    # TensorFlow
    "tensorflow framework": "TensorFlow",

    # PyTorch
    "pytorch framework": "PyTorch"
}


# ============================================================
# SKILL -> CATEGORY MAPPING
# ============================================================

SKILL_CATEGORY = {}

for category, skill_list in SKILL_TAXONOMY.items():

    for skill in skill_list:

        if skill not in SKILL_CATEGORY:

            SKILL_CATEGORY[skill] = category


# ============================================================
# FLAT SKILL LIST
# ============================================================

ALL_SKILLS = []

for skill_list in SKILL_TAXONOMY.values():

    ALL_SKILLS.extend(skill_list)


# Remove duplicate skills
ALL_SKILLS = list(
    dict.fromkeys(ALL_SKILLS)
)


# ============================================================
# PREPROCESSING
# ============================================================

def preprocess_text(text):
    """
    Clean and normalize input job description.
    """

    text = str(text)

    # Convert to lowercase
    text = text.lower()

    # Replace multiple spaces with single space
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# DICTIONARY-BASED EXTRACTION
# ============================================================

def dictionary_extract(text):
    """
    Extract skills using taxonomy-based matching.
    """

    text = preprocess_text(text)

    found_skills = []

    for skill in ALL_SKILLS:

        skill_lower = skill.lower()

        pattern = (
            r"(?<!\w)"
            + re.escape(skill_lower)
            + r"(?!\w)"
        )

        if re.search(pattern, text):

            found_skills.append(skill)

    return list(
        dict.fromkeys(found_skills)
    )


# ============================================================
# REGEX EXTRACTION
# ============================================================

def regex_matching(text):
    """
    Extract skills using regular expressions.
    """

    text = str(text)

    found_skills = set()

    for skill in ALL_SKILLS:

        pattern = (
            r"(?<!\w)"
            + re.escape(skill)
            + r"(?!\w)"
        )

        if re.search(
            pattern,
            text,
            re.IGNORECASE
        ):

            found_skills.add(skill)

    return list(found_skills)


# ============================================================
# SKILL NORMALIZATION
# ============================================================

def normalize_skill(skill):
    """
    Convert skill variations into standard names.
    """

    skill = str(skill).strip().lower()

    # Check normalization dictionary
    if skill in SKILL_NORMALIZATION:

        return SKILL_NORMALIZATION[skill]

    # Check taxonomy
    for standard_skill in ALL_SKILLS:

        if standard_skill.lower() == skill:

            return standard_skill

    return skill.title()


def normalize_skills(skills):
    """
    Normalize skills and remove duplicates.
    """

    normalized = []

    for skill in skills:

        normalized_skill = normalize_skill(
            skill
        )

        if normalized_skill not in normalized:

            normalized.append(
                normalized_skill
            )

    return normalized


# ============================================================
# CATEGORY MAPPING
# ============================================================

def get_skill_category(skill):
    """
    Return category for a given skill.
    """

    # Direct match
    if skill in SKILL_CATEGORY:

        return SKILL_CATEGORY[skill]

    # Case-insensitive match
    skill_lower = skill.lower()

    for skill_name, category in SKILL_CATEGORY.items():

        if skill_name.lower() == skill_lower:

            return category

    return "Unknown"


def get_categories(skill_list):
    """
    Return unique categories for detected skills.
    """

    categories = []

    for skill in skill_list:

        category = get_skill_category(
            skill
        )

        if (
            category != "Unknown"
            and category not in categories
        ):

            categories.append(category)

    return categories


# ============================================================
# SEMANTIC MODEL
# ============================================================

@lru_cache(maxsize=1)
def load_semantic_model():
    """
    Load Sentence Transformer model only once.
    """

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    return model


# ============================================================
# SKILL EMBEDDINGS
# ============================================================

@lru_cache(maxsize=1)
def load_skill_embeddings():
    """
    Generate embeddings for all taxonomy skills.
    """

    model = load_semantic_model()

    embeddings = model.encode(
        ALL_SKILLS,
        convert_to_numpy=True
    )

    return embeddings


# ============================================================
# SEMANTIC EXTRACTION
# ============================================================

def semantic_extract(
    text,
    threshold=0.45
):
    """
    Extract skills using semantic similarity.
    """

    from sklearn.metrics.pairwise import cosine_similarity

    model = load_semantic_model()

    skill_embeddings = load_skill_embeddings()

    text_embedding = model.encode(
        str(text),
        convert_to_numpy=True
    )

    similarity_scores = cosine_similarity(
        text_embedding.reshape(1, -1),
        skill_embeddings
    )[0]

    matched_skills = []

    for index, score in enumerate(
        similarity_scores
    ):

        if score >= threshold:

            matched_skills.append(
                ALL_SKILLS[index]
            )

    return matched_skills


# ============================================================
# FINAL SKILL EXTRACTION PIPELINE
# ============================================================

def extract_skills(text):
    """
    Complete NLP skill extraction pipeline.

    Pipeline:
    1. Preprocessing
    2. Dictionary Extraction
    3. Regex Extraction
    4. Semantic Similarity
    5. Skill Normalization
    6. Duplicate Removal
    7. Category Mapping
    """

    # --------------------------------------------------------
    # Step 1: Preprocessing
    # --------------------------------------------------------

    cleaned_text = preprocess_text(
        text
    )


    # --------------------------------------------------------
    # Step 2: Dictionary Extraction
    # --------------------------------------------------------

    dictionary_skills = dictionary_extract(
        cleaned_text
    )


    # --------------------------------------------------------
    # Step 3: Regex Extraction
    # --------------------------------------------------------

    regex_skills = regex_matching(
        cleaned_text
    )


    # --------------------------------------------------------
    # Step 4: Semantic Extraction
    # --------------------------------------------------------

    semantic_skills = semantic_extract(
        cleaned_text,
        threshold=0.45
    )


    # --------------------------------------------------------
    # Step 5: Combine Extraction Results
    # --------------------------------------------------------

    combined_skills = (
        dictionary_skills
        + regex_skills
        + semantic_skills
    )


    # --------------------------------------------------------
    # Step 6: Normalize Skills
    # --------------------------------------------------------

    normalized_skills = normalize_skills(
        combined_skills
    )


    # --------------------------------------------------------
    # Step 7: Remove Duplicates
    # --------------------------------------------------------

    final_skills = list(
        dict.fromkeys(
            normalized_skills
        )
    )


    # --------------------------------------------------------
    # Step 8: Category Mapping
    # --------------------------------------------------------

    categories = get_categories(
        final_skills
    )


    return final_skills, categories


# ============================================================
# DETAILED EXTRACTION
# ============================================================

def extract_skills_detailed(text):
    """
    Return detailed results from every extraction method.
    """

    cleaned_text = preprocess_text(
        text
    )


    # Dictionary extraction
    dictionary_skills = dictionary_extract(
        cleaned_text
    )


    # Regex extraction
    regex_skills = regex_matching(
        cleaned_text
    )


    # Semantic extraction
    semantic_skills = semantic_extract(
        cleaned_text
    )


    # Combine results
    combined_skills = (
        dictionary_skills
        + regex_skills
        + semantic_skills
    )


    # Normalize
    final_skills = normalize_skills(
        combined_skills
    )


    # Remove duplicates
    final_skills = list(
        dict.fromkeys(
            final_skills
        )
    )


    # Category mapping
    categories = get_categories(
        final_skills
    )


    return {
        "skills": final_skills,
        "categories": categories,
        "dictionary_skills": dictionary_skills,
        "regex_skills": regex_skills,
        "semantic_skills": semantic_skills
    }