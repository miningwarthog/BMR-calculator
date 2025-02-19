import streamlit as st

def calculate_bmi(weight, height):
    if height <= 0 or weight <= 0:
        return None
    return weight / (height / 100) ** 2

def calculate_bmr(gender, weight, height, age):
    if gender == "Male":
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == "Female":
        return (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        return None  # Handle invalid gender

def calculate_macronutrients(bmr):
    if bmr is None or bmr <= 0:
        return None
    carbon_hydrate = (0.5 * bmr) / 4
    protein = (0.3 * bmr) / 4
    fat = (0.2 * bmr) / 9
    bread = 0.5 * carbon_hydrate  # Assuming 50% of carbs from bread
    chicken_breast = 0.27 * protein  # Assuming 27% of protein from chicken
    butter = 0.81 * fat  # Assuming 81% of fat from butter
    return carbon_hydrate, protein, fat, bread, chicken_breast, butter

st.title("Body Status Calculator")

gender = st.selectbox("Select your gender", ["Male", "Female"])
age = st.number_input("Enter your age", min_value=1, max_value=120, step=1)
height = st.number_input("Enter your height in cm", min_value=50, max_value=250, step=1)
weight = st.number_input("Enter your weight in kg", min_value=10, max_value=300, step=1)

if st.button("Calculate"):
    if height == 0 or weight == 0:
        st.error("Height and weight must be greater than zero.")
    else:
        bmi = calculate_bmi(weight, height)
        bmr = calculate_bmr(gender, weight, height, age)

        if bmr is None:
            st.error("Invalid gender selection.")
        else:
            # Determine calorie adjustment based on BMI
            if bmi < 18.5:
                st.warning("You are underweight. Increase your calorie intake.")
                standard_weight = 19 * (height / 100) ** 2
                standard_bmr = calculate_bmr(gender, standard_weight, height, age) + 200
            elif bmi < 25:
                st.success("You are in a healthy weight range. Keep up the good work!")
                standard_weight = weight
                standard_bmr = bmr + 200
            else:
                st.error("You are overweight. Reduce your calorie intake.")
                standard_weight = 25 * (height / 100) ** 2
                standard_bmr = calculate_bmr(gender, standard_weight, height, age) - 200  # Adjusted BMR

            # Calculate macronutrient intake
            nutrients = calculate_macronutrients(standard_bmr)
            if nutrients:
                carbon_hydrate, protein, fat, bread, chicken_breast, butter = nutrients
                st.write(f"Your suggested daily calorie intake: **{standard_bmr:.0f} Kcal**")
                st.write(f"Suggested carbohydrate intake: **{carbon_hydrate:.0f}g**")
                st.write(f"Suggested protein intake: **{protein:.0f}g**")
                st.write(f"Suggested fat intake: **{fat:.0f}g**")

                st.write(f"These nutrients can be converted into:")
                st.write(f"🍞 **{bread:.0f}g** of bread")
                st.write(f"🍗 **{chicken_breast:.0f}g** of chicken breast")
                st.write(f"🧈 **{butter:.0f}g** of butter")
            else:
                st.error("Invalid BMR calculation. Check your inputs.")
        
        st.write(f"These nutrients can be converted into: ")
        st.write(f"🍞 **{bread:.0f}g** of bread")
        st.write(f"🍗 **{chicken_breast:.0f}g** of chicken breast")
        st.write(f"🧈 **{butter:.0f}g** of butter")
