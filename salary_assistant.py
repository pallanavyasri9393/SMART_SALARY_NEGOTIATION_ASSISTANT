# ================================
# SALARY NEGOTIATION ASSISTANT
# Beginner Friendly Version
# ================================

# Step 1: Define skill values
skill_values = {
    "python": 2,
    "sql": 2,
    "excel": 1,
    "ml": 3,
    "data analysis": 2,
    "deep learning": 4,
    "java": 2
}

# Step 2: Function to calculate salary
def calculate_salary(skills, experience, location):

    # calculate skill score
    skill_score = 0
    for skill in skills:
        skill_score += skill_values.get(skill, 1)

    # base salary calculation
    base_salary = skill_score * 2

    # experience factor
    experience_factor = 1 + (experience * 0.1)

    # location factor
    if location == "bangalore":
        location_factor = 1.3
    elif location == "hyderabad":
        location_factor = 1.1
    else:
        location_factor = 1.0

    # final salary
    final_salary = base_salary * experience_factor * location_factor

    return round(final_salary, 2)

# ================================
# Step 3: Take user input
# ================================

print("\n--- Salary Negotiation Assistant ---\n")

skills_input = input("Enter your skills (comma separated): ")
skills_list = skills_input.lower().split(",")

experience = int(input("Enter your years of experience: "))
location = input("Enter your location (Bangalore/Hyderabad/Pune): ").lower()

# ================================
# Step 4: Salary Prediction
# ================================

salary = calculate_salary(skills_list, experience, location)

min_salary = round(salary * 0.9, 2)
max_salary = round(salary * 1.1, 2)

# ================================
# Step 5: Output
# ================================

print("\nRecommended Salary Range:")
print(f"₹ {min_salary} LPA  -  ₹ {max_salary} LPA")

if experience < 1:
    print("Advice: Focus on learning. Entry-level salaries have limited negotiation.")
elif experience < 3:
    print("Advice: You can negotiate moderately based on your skills.")
else:
    print("Advice: You can confidently negotiate a higher salary.")
