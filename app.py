# ======================================================
# SMART SALARY NEGOTIATION ASSISTANT
# (BEGINNER FRIENDLY – NO ML, NO GRAPHS)
# ======================================================

import streamlit as st

# ======================================================
# PAGE CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="Smart Salary Negotiation Assistant",
    layout="centered"
)

# ======================================================
# CUSTOM UI STYLE
# ======================================================
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #141E30, #243B55);
}
.main {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 35px;
    border-radius: 18px;
}
h1 {
    text-align: center;
    color: #0A2647;
}
h3 {
    text-align: center;
    color: #144272;
    font-weight: 400;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# HERO SECTION
# ======================================================
st.markdown("<h1>Smart Salary Negotiation Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h3>Know your worth before you negotiate.</h3>", unsafe_allow_html=True)

st.write(
    "This tool estimates a fair salary range based on your "
    "skills, experience, and job location — and explains why."
)

st.write("---")

# ======================================================
# SKILL VALUES
# ======================================================
skill_values = {
    "Python": 2,
    "SQL": 2,
    "Excel": 1,
    "Machine Learning": 3,
    "Data Analysis": 2,
    "Deep Learning": 4,
    "Java": 2
}

# ======================================================
# USER INPUTS
# ======================================================
st.markdown("### 👤 Tell Us About You")

experience_option = st.selectbox(
    "Years of Experience",
    ["Fresher (0 years)", "1 year", "2 years", "3 years", "4 years", "5+ years"]
)

experience_map = {
    "Fresher (0 years)": 0,
    "1 year": 1,
    "2 years": 2,
    "3 years": 3,
    "4 years": 4,
    "5+ years": 5
}
experience = experience_map[experience_option]

location = st.selectbox(
    "Preferred Job Location",
    ["Bangalore", "Hyderabad", "Pune", "Other"]
)

st.subheader("Select Your Skills")
selected_skills = []
for skill in skill_values:
    if st.checkbox(skill):
        selected_skills.append(skill)

# ======================================================
# SIMPLE RULE-BASED SALARY FUNCTION
# ======================================================
def calculate_salary(skills, experience, location):
    skill_score = sum(skill_values.get(skill, 1) for skill in skills)
    base_salary = skill_score * 2  # base in LPA

    experience_factor = 1 + (experience * 0.15)

    location_factor = {
        "Bangalore": 1.3,
        "Hyderabad": 1.1,
        "Pune": 1.0,
        "Other": 0.9
    }

    final_salary = base_salary * experience_factor * location_factor[location]
    return round(final_salary, 2)

# ======================================================
# BUTTON ACTION
# ======================================================
if st.button("💰 Calculate My Salary"):

    if not selected_skills:
        st.warning("Please select at least one skill.")
    else:
        salary = calculate_salary(selected_skills, experience, location)

        min_salary = round(salary * 0.9, 2)
        max_salary = round(salary * 1.1, 2)

        # ======================================================
        # OUTPUT
        # ======================================================
        st.success(f"Recommended Salary Range: ₹ {min_salary} – ₹ {max_salary} LPA")

        # ======================================================
        # SALARY EXPLANATION
        # ======================================================
        st.markdown("### 📌 Why this salary range?")

        st.write(f"""
        *1️⃣ Skills Selected:*  
        You selected *{len(selected_skills)} skills*, increasing your base salary.

        *2️⃣ Experience Level:*  
        With *{experience} years of experience*, your value increases due to expertise.

        *3️⃣ Job Location:*  
        Salaries in *{location}* vary based on demand and living costs.

        *4️⃣ Calculation Method:*  
        This salary is calculated using a *simple rule-based logic*, making it transparent and easy to understand.
        """)

        # ======================================================
        # NEGOTIATION ADVICE
        # ======================================================
        if experience == 0:
            st.info("💡 Advice: Focus on learning and entry-level opportunities.")
        elif experience <= 2:
            st.info("💡 Advice: Negotiate carefully using skills and internships/projects.")
        else:
            st.info("💡 Advice: You can confidently negotiate based on experience and skills.")