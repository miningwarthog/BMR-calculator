# What is your BMI status?


# Introduction

This research aims to find out the factors that affect BMI (Body Mass Index) and discuss possible solutions to control BMI within a healthy range. BMI is a numerical value derived from a person's weight and height. It is calculated using the formula:

BMI = Weight(kg)/Height(cm)^2

BMI is commonly used to categorize individuals into different weight status groups, such as underweight, normal weight, overweight, and obesity. However, it does not directly measure body fat and may not accurately reflect health status for all individuals.

The dataset in this research is taken from Kaggle. The raw dataset contains 9 columns.

This research is going to use Microsoft Excel and PowerBI for exploratory analysis and Python for coding. Both Excel file and PowerBI file can be accessed through file list 


# Exploratory Analysis

The raw dataset has been cleansed and the participants' BMI have been catogerised into three categories in a new column 'BMI Status'. BMI status will be 'Underweight' if BMI is less than 19, will be 'Healthy' if BMI is between 19 and 25, and will be 'Overweight' if BMI is greater than 25. 


![BMI ALL excel](https://github.com/user-attachments/assets/8decc380-749b-48ce-b2ea-f8fbe272b3a0)
![bmi femal excel](https://github.com/user-attachments/assets/8f1221a2-6252-483f-ab1a-5019a3b12a82)
![bmi male excel](https://github.com/user-attachments/assets/ff86fbc8-6c8f-4151-af11-da09cac54a8c)

The visualisations above indicate that there are higher proportion of overweight male participants than female participants. And the BMI tends to increase with age, and this increasing trend is more significant with male.

![bmi_all](https://github.com/user-attachments/assets/cae4b637-c4b0-42d8-9a5a-719b24c1b191)
![bmi_female](https://github.com/user-attachments/assets/38041fb4-1d8d-44a3-96d9-14ddb9c4b6c4)
![bmi_male](https://github.com/user-attachments/assets/b2f24247-be9a-48fd-bbcf-953fc50f4137)

And these three visualisations from Power BI indicate that both Body Temperature Duration Time have positive relationships with Calories. Which means that higher intensity and longer duration of each exercise have more significant effect in burning calories. Also, this effect is more significant for female than male for that the curves of female are steeper than male's. 


# BMI Calculator

To calculate whether one's BMI is within a healthy range, Python and Streamlit are used. User can input body status and the calculator will return the BMI status, suggested daily intake calories and suggested diet. Three major nutrients are converted into bread, chicken breast and butter for easier understanding. Below are some code examples and the complete Python code can be found in the file list.

```bash
  import streamlit as st

  def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

  def calculate_bmr(gender, weight, height, age):
    if gender == "Male":
        return (10 * weight) + (6.25 * height) - (5 * age)
    elif gender == "Female":
        return (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        return None
  ...
    carbon_hydrate, protein, fat, bread, chicken_breast, butter = calculate_macronutrients(standard_bmr)
        
    st.write(f"Your suggested daily calorie intake: **{standard_bmr:.0f} Kcal**")
    st.write(f"Suggested carbohydrate intake: **{carbon_hydrate:.0f}g**")
    st.write(f"Suggested protein intake: **{protein:.0f}g**")
    st.write(f"Suggested fat intake: **{fat:.0f}g**")
        
    st.write(f"These nutrients can be converted into: ")
    st.write(f"🍞 **{bread:.0f}g** of bread")
    st.write(f"🍗 **{chicken_breast:.0f}g** of chicken breast")
    st.write(f"🧈 **{butter:.0f}g** of butter")
  ```

Here is the link to the calculator and an example of its output.
![image](https://github.com/user-attachments/assets/14275063-9a0d-47dc-b129-845a076e6b96)

https://what-is-your-bmi-status-ir9ahnkmu2svzr5afh7sar.streamlit.app/


# Conclusion

Based on this research, these conclusions can be drawn:
* Male is more likely to be overweight that female.
* As age increases, BMI is likely to increase as well.
* Intensive and long-duration exercises have positive influences on burning calories.
* These positive effects are more significant for female than male.

Certainly, there are several drawbacks in this research:
* The dataset is very likely to have selection bias because it is taken from a sport app, where the users are the people mostly with work-out habits. There is no access to the data of people who do not do sports. Therefore we can not conclude a more general conclusion and it is remained unknown to the factors of obesity or underweight in some extreme cases.
* The sample size is limited, there may be other confoundings can affect BMI.
* No formal analysis has been conducted so we can not conclude more precisely numerical or logical relationships between BMI and other factors.   
