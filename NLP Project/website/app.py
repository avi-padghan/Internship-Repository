import streamlit as st
import json
import hashlib
import re
from pathlib import Path

from utils.skill_extractor import (
    extract_skills,
    get_skill_category
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SkillSense",
    page_icon="💼",
    layout="wide"
)


# ============================================================
# FILE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = BASE_DIR / "users.json"


# ============================================================
# HTML HELPER
# ============================================================

def render_html(content):
    """
    Render HTML without leading indentation.

    Streamlit can treat indented HTML as a Markdown code block.
    This helper removes indentation from every HTML line.
    """
    content = re.sub(r"(?m)^[ \t]+", "", content)
    st.markdown(content, unsafe_allow_html=True)


# ============================================================
# USER MANAGEMENT
# ============================================================

def hash_password(password):
    """Create a SHA-256 password hash."""
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


def save_users(users):
    """Save users to users.json."""
    with open(
        USERS_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            users,
            file,
            indent=4
        )


def load_users():
    """Load users from users.json."""

    if not USERS_FILE.exists():

        default_users = {
            "admin@skillsense.com": {
                "name": "Admin",
                "password": hash_password("admin123")
            }
        }

        save_users(default_users)

        return default_users

    try:

        with open(
            USERS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except (json.JSONDecodeError, OSError):

        return {}


users = load_users()


# ============================================================
# SESSION STATE
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "login"

if "registration_message" not in st.session_state:
    st.session_state.registration_message = ""

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "show_about" not in st.session_state:
    st.session_state.show_about = False

if "show_how_it_works" not in st.session_state:
    st.session_state.show_how_it_works = False


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
"""
<style>

/* ============================================================
   GLOBAL
   ============================================================ */

.stApp {
    background-color: #F8FAFC;
    color: #1E293B;
}

header {
    visibility: hidden;
}

.block-container {
    max-width: 1200px;
    width: 100%;
    padding-top: 1rem;
    padding-bottom: 1.5rem;
    margin: auto;
}


/* ============================================================
   LOGIN BRAND CARD
   ============================================================ */

.login-card {
    background-color: #FFFFFF;
    border: 1px solid #BFDBFE;
    border-radius: 16px;
    padding: 35px 45px;
    margin: 25px auto 25px auto;
    text-align: center;
    box-shadow: 0 8px 25px rgba(15, 23, 42, 0.08);
}

.login-title {
    color: #1E3A8A;
    font-size: 52px;
    font-weight: 800;
    line-height: 1.1;
}

.login-subtitle {
    color: #2563EB;
    font-size: 20px;
    margin-top: 8px;
}


/* ============================================================
   AUTH PAGE
   ============================================================ */

.auth-title {
    color: #1E293B;
    font-size: 34px;
    font-weight: 750;
    text-align: center;
    margin: 18px 0;
}

.auth-help {
    color: #64748B;
    font-size: 17px;
    text-align: center;
    margin: 12px 0;
}


/* ============================================================
   AUTH TAB INDICATOR
   ============================================================ */

.active-auth-label {
    text-align: center;
    color: #1D4ED8;
    font-size: 17px;
    font-weight: 700;
    margin: 5px 0 12px 0;
}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {
    background-color: #2563EB;
    color: #FFFFFF;
    border: none;
    border-radius: 9px;
    min-height: 52px;
    font-size: 17px;
    font-weight: 650;
}

.stButton > button:hover {
    background-color: #1D4ED8;
    color: #FFFFFF;
}

.auth-button .stButton > button {
    min-height: 62px !important;
    font-size: 20px !important;
    font-weight: 750 !important;
    border-radius: 10px !important;
}


/* ============================================================
   INPUTS
   ============================================================ */

div[data-baseweb="input"] {
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 8px !important;
}

div[data-baseweb="input"] input {
    background-color: #FFFFFF !important;
    color: #1E293B !important;
    -webkit-text-fill-color: #1E293B !important;
    font-size: 18px !important;
}

div[data-baseweb="textarea"] {
    background-color: #FFFFFF !important;
    border-radius: 10px !important;
    border: 1px solid #CBD5E1 !important;
}

div[data-baseweb="textarea"] textarea {
    background-color: #FFFFFF !important;
    color: #1E293B !important;
    -webkit-text-fill-color: #1E293B !important;
    font-size: 19px !important;
    line-height: 1.6 !important;
}



/* ============================================================
   CLEAR FOCUS STATE
   ============================================================ */

div[data-baseweb="input"]:focus-within {
    border: 2px solid #2563EB !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
}

div[data-baseweb="textarea"]:focus-within {
    border: 2px solid #2563EB !important;
    box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.15) !important;
}

div[data-baseweb="input"] input:focus {
    outline: none !important;
}

div[data-baseweb="textarea"] textarea:focus {
    outline: none !important;
}

/* Make text cursor and active typing area obvious */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    caret-color: #2563EB !important;
}


/* ============================================================
   MAIN HEADER
   ============================================================ */

.navbar {
    background-color: #DBEAFE;
    border: 1px solid #BFDBFE;
    border-radius: 14px;
    padding: 20px 24px;
    text-align: center;
    margin-bottom: 8px;
}

.navbar-title {
    color: #1E3A8A;
    font-size: 46px;
    font-weight: 800;
    line-height: 1.1;
}

.navbar-subtitle {
    color: #2563EB;
    font-size: 19px;
    margin-top: 5px;
}


/* ============================================================
   USER WELCOME
   ============================================================ */

.welcome-user {
    color: #1E293B;
    font-size: 28px;
    font-weight: 750;
    text-align: center;
    margin: 10px 0 15px 0;
}


/* ============================================================
   SECTION
   ============================================================ */

.section-title {
    color: #1E293B;
    font-size: 36px;
    font-weight: 750;
    text-align: center;
    margin: 12px 0;
}

.section-description {
    color: #64748B;
    font-size: 20px;
    text-align: center;
    margin-bottom: 18px;
    line-height: 1.5;
}


/* ============================================================
   INFORMATION BOX
   ============================================================ */

.info-box {
    background-color: #FFFFFF;
    border: 1px solid #BFDBFE;
    border-left: 5px solid #06B6D4;
    border-radius: 9px;
    padding: 20px 22px;
    margin-top: 15px;
    color: #475569;
    font-size: 18px;
    line-height: 1.75;
}


/* ============================================================
   METRIC CARDS
   ============================================================ */

.metric-card {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 3px 10px rgba(15, 23, 42, 0.04);
}

.metric-value {
    color: #2563EB;
    font-size: 42px;
    font-weight: 750;
}

.metric-label {
    color: #64748B;
    font-size: 19px;
    margin-top: 7px;
}


/* ============================================================
   RESULTS
   ============================================================ */

.result-title {
    color: #1E293B;
    font-size: 38px;
    font-weight: 750;
    text-align: center;
    margin-top: 30px;
    margin-bottom: 18px;
}

.table-header {
    background-color: #DBEAFE;
    color: #1E3A8A;
    padding: 13px;
    text-align: center;
    font-weight: 700;
    font-size: 19px;
    border-radius: 8px;
    border: 1px solid #BFDBFE;
}

.skill-badge {
    display: block;
    background-color: #ECFDF5;
    color: #16A34A;
    padding: 12px;
    border-radius: 8px;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    border: 1px solid #BBF7D0;
}

.category-badge {
    display: block;
    background-color: #EFF6FF;
    color: #2563EB;
    padding: 12px;
    border-radius: 8px;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    border: 1px solid #BFDBFE;
}

.status-success {
    color: #16A34A;
    font-weight: 650;
    text-align: center;
    padding-top: 12px;
    font-size: 18px;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    color: #64748B;
    font-size: 15px;
    padding-top: 25px;
}

</style>
""",
unsafe_allow_html=True
)


# ============================================================
# LOGIN / REGISTER PAGE
# ============================================================

if not st.session_state.logged_in:

    render_html(
"""
<div class="login-card">
<div class="login-title">SkillSense</div>
<div class="login-subtitle">Intelligent Job Skill Analysis</div>
</div>
"""
    )

    # ========================================================
    # LOGIN FORM
    # ========================================================

    if st.session_state.auth_mode == "login":

        render_html(
"""
<div class="active-auth-label">🔐 LOGIN • Active</div>
<div class="auth-title">Welcome Back</div>
"""
        )

        if st.session_state.registration_message:

            st.success(
                st.session_state.registration_message
            )

            st.session_state.registration_message = ""

        email = st.text_input(
            "Email",
            placeholder="Enter your email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            key="login_password"
        )

        login_left, login_center, login_right = st.columns(
            [1, 1.2, 1]
        )

        with login_center:

            login = st.button(
                "🔐  LOGIN",
                use_container_width=True,
                key="login_submit"
            )

        if login:

            email_clean = email.strip().lower()

            if not email_clean:

                st.error(
                    "Please enter your email."
                )

            elif not password:

                st.error(
                    "Please enter your password."
                )

            elif email_clean not in users:

                st.error(
                    "Account not found. Please register first."
                )

            elif users[email_clean]["password"] != hash_password(password):

                st.error(
                    "Incorrect password."
                )

            else:

                st.session_state.logged_in = True
                st.session_state.user_name = users[email_clean]["name"]
                st.session_state.user_email = email_clean

                st.rerun()


        render_html(
"""
<div class="auth-help">
Don't have an account? Register below.
</div>
"""
        )

        st.markdown(
            '<div class="auth-button">',
            unsafe_allow_html=True
        )

        register_option = st.button(
            "📝  REGISTER",
            use_container_width=True,
            key="register_option"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        if register_option:

            st.session_state.auth_mode = "register"
            st.rerun()


        render_html(
"""
<div class="footer">
Demo Login: admin@skillsense.com | Password: admin123
</div>
"""
        )


    # ========================================================
    # REGISTER FORM
    # ========================================================

    else:

        render_html(
"""
<div class="active-auth-label">📝 REGISTER • Active</div>
<div class="auth-title">Create Your Account</div>
"""
        )

        name = st.text_input(
            "Full Name",
            placeholder="Enter your full name",
            key="register_name"
        )

        register_email = st.text_input(
            "Email",
            placeholder="Enter your email",
            key="register_email"
        )

        register_password = st.text_input(
            "Password",
            type="password",
            placeholder="Create a password",
            key="register_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Re-enter your password",
            key="confirm_password"
        )

        register_left, register_center, register_right = st.columns(
            [1, 1.2, 1]
        )

        with register_center:

            register = st.button(
                "📝  REGISTER",
                use_container_width=True,
                key="register_submit"
            )

        if register:

            name_clean = name.strip()
            email_clean = register_email.strip().lower()

            if not name_clean:

                st.error(
                    "Please enter your full name."
                )

            elif not email_clean:

                st.error(
                    "Please enter your email."
                )

            elif "@" not in email_clean or "." not in email_clean:

                st.error(
                    "Please enter a valid email address."
                )

            elif len(register_password) < 6:

                st.error(
                    "Password must contain at least 6 characters."
                )

            elif register_password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            elif email_clean in users:

                st.error(
                    "This email is already registered. Please login."
                )

            else:

                users[email_clean] = {
                    "name": name_clean,
                    "password": hash_password(register_password)
                }

                save_users(users)

                st.session_state.auth_mode = "login"

                st.session_state.registration_message = (
                    f"Registration successful for {name_clean}! "
                    "Please login below."
                )

                st.rerun()


        render_html(
"""
<div class="auth-help">
Already have an account? Login below.
</div>
"""
        )

        st.markdown(
            '<div class="auth-button">',
            unsafe_allow_html=True
        )

        login_option = st.button(
            "🔐  LOGIN",
            use_container_width=True,
            key="login_option"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        if login_option:

            st.session_state.auth_mode = "login"
            st.rerun()


# ============================================================
# MAIN APPLICATION
# ============================================================

else:

    # ========================================================
    # HEADER
    # ========================================================

    render_html(
"""
<div class="navbar">
<div class="navbar-title">SkillSense</div>
<div class="navbar-subtitle">Intelligent Job Skill Analysis</div>
</div>
"""
    )


    # ========================================================
    # TOP RIGHT ACTIONS
    # ========================================================

    top_space, top_about, top_logout = st.columns(
        [8.4, 1.1, 1.1]
    )

    with top_about:

        st.markdown(
            '<div class="top-right-button">',
            unsafe_allow_html=True
        )

        if st.button(
            "ℹ About",
            use_container_width=True,
            key="top_about"
        ):

            st.session_state.show_about = True
            st.session_state.show_how_it_works = False
            st.rerun()

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    with top_logout:

        st.markdown(
            '<div class="top-right-button">',
            unsafe_allow_html=True
        )

        if st.button(
            "🚪 Logout",
            use_container_width=True,
            key="top_logout"
        ):

            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.session_state.user_email = ""
            st.session_state.job_description = ""
            st.session_state.show_about = False
            st.session_state.show_how_it_works = False
            st.session_state.auth_mode = "login"

            st.rerun()

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # WELCOME USER
    # ========================================================

    render_html(
f"""
<div class="welcome-user">
Welcome to SkillSense, {st.session_state.user_name}! 👋
</div>
"""
    )


    # ========================================================
    # MAIN NAVIGATION
    # ========================================================

    nav_left, nav_home, nav_how, nav_reset, nav_right = st.columns(
        [1, 1.2, 1.2, 1.2, 1]
    )


    with nav_home:

        if st.button(
            "⌂ Home",
            use_container_width=True,
            key="home_button"
        ):

            st.session_state.show_about = False
            st.session_state.show_how_it_works = False
            st.rerun()


    with nav_how:

        if st.button(
            "⚙ How It Works",
            use_container_width=True,
            key="how_button"
        ):

            st.session_state.show_about = False
            st.session_state.show_how_it_works = True
            st.rerun()


    with nav_reset:

        if st.button(
            "↻ Reset",
            use_container_width=True,
            key="reset_button"
        ):

            st.session_state.job_description = ""
            st.session_state.show_about = False
            st.session_state.show_how_it_works = False
            st.rerun()


    # ========================================================
    # ABOUT PAGE
    # ========================================================

    if st.session_state.show_about:

        render_html(
"""
<div class="section-title">About SkillSense</div>

<div class="info-box">

<b>SkillSense</b> is an NLP-based Job Skill Analysis
application designed to identify technical skills from
Job Descriptions.

<br><br>

The application extracts relevant skills and maps them
to technology categories such as Programming, Database,
Data Libraries, Data Visualization, BI Tools,
Spreadsheet Tools, Cloud and DevOps.

</div>
"""
        )


    # ========================================================
    # HOW IT WORKS
    # ========================================================

    elif st.session_state.show_how_it_works:

        render_html(
"""
<div class="section-title">How SkillSense Works</div>

<div class="info-box">

<b>1. Job Description</b><br>
User enters or pastes a Job Description.

<br><br>

<b>2. Preprocessing</b><br>
The text is cleaned and normalized.

<br><br>

<b>3. Skill Extraction</b><br>
Dictionary matching, Regex matching and Semantic
Similarity identify relevant skills.

<br><br>

<b>4. Skill Normalization</b><br>
Different forms of the same skill are converted
into a standard skill name.

<br><br>

<b>5. Category Mapping</b><br>
Each detected skill is mapped to its technology category.

<br><br>

<b>6. Final Results</b><br>
Detected skills, categories and analysis status
are displayed.

</div>
"""
        )


    # ========================================================
    # HOME PAGE
    # ========================================================

    else:

        render_html(
"""
<div class="section-title">Job Description</div>

<div class="section-description">
Paste a job description below to identify relevant
skills and technology categories.
</div>
"""
        )


        job_description = st.text_area(
            "Job Description",
            value=st.session_state.job_description,
            placeholder=(
                "Example:\n\n"
                "Looking for Data Analyst with Python, SQL, "
                "Pandas, Power BI and Excel experience."
            ),
            height=180,
            label_visibility="collapsed"
        )

        st.session_state.job_description = job_description

        button_left, button_center, button_right = st.columns(
            [1, 1.2, 1]
        )

        with button_center:

            analyze = st.button(
                "🔍 Analyze Description",
                use_container_width=True,
                key="analyze_button"
            )


        # ====================================================
        # NLP ANALYSIS
        # ====================================================

        if analyze:

            if not job_description.strip():

                st.error(
                    "Please enter a Job Description."
                )

            else:

                with st.spinner(
                    "Analyzing Job Description..."
                ):

                    detected_skills, categories = extract_skills(
                        job_description
                    )


                render_html(
f"""
<div class="result-title">Analysis Results</div>
"""
                )


                # ------------------------------------------------
                # METRICS
                # ------------------------------------------------

                col1, col2, col3 = st.columns(3)


                with col1:

                    render_html(
f"""
<div class="metric-card">
<div class="metric-value">{len(detected_skills)}</div>
<div class="metric-label">Skills Detected</div>
</div>
"""
                    )


                with col2:

                    render_html(
f"""
<div class="metric-card">
<div class="metric-value">{len(categories)}</div>
<div class="metric-label">Categories</div>
</div>
"""
                    )


                with col3:

                    render_html(
"""
<div class="metric-card">
<div class="metric-value">✓</div>
<div class="metric-label">Analysis Complete</div>
</div>
"""
                    )


                # =================================================
                # DETECTED SKILLS
                # =================================================

                if detected_skills:

                    render_html(
"""
<div class="section-title">Detected Skills</div>

<div class="section-description">
Skills identified using the NLP extraction pipeline.
</div>
"""
                    )


                    header1, header2, header3 = st.columns(3)


                    with header1:

                        render_html(
"""
<div class="table-header">Skill</div>
"""
                        )


                    with header2:

                        render_html(
"""
<div class="table-header">Category</div>
"""
                        )


                    with header3:

                        render_html(
"""
<div class="table-header">Status</div>
"""
                        )


                    # ------------------------------------------------
                    # SKILL ROWS
                    # ------------------------------------------------

                    for skill in detected_skills:

                        category = get_skill_category(
                            skill
                        )

                        col1, col2, col3 = st.columns(3)


                        with col1:

                            render_html(
f"""
<div class="skill-badge">{skill}</div>
"""
                            )


                        with col2:

                            render_html(
f"""
<div class="category-badge">{category}</div>
"""
                            )


                        with col3:

                            render_html(
"""
<div class="status-success">✓ Detected</div>
"""
                            )


                else:

                    st.warning(
                        "No relevant skills were detected."
                    )


    # ========================================================
    # FOOTER
    # ========================================================

    render_html(
"""
<div class="footer">
SkillSense • Intelligent Job Skill Analysis • By Avi Padghan
</div>
"""
    )
