# Student Dropout Prediction

## Business Understanding

### Business Background
Jaya Jaya Institute is an established educational institution that has been operating since 2000. Over the years, it has produced numerous graduates with a strong reputation. However, the institute faces a significant issue of high dropout rates among its students. This not only tarnishes the institution's reputation but also negatively impacts students who fail to complete their education.

### Business Problem
The main challenge faced by Jaya Jaya Institute is the high number of students who do not complete their education, commonly referred to as dropout. This issue has several urgent implications:
1. **Reputation Damage**: High dropout rates can harm the institution's reputation, making it less attractive to potential students and stakeholders.
2. **Financial Loss**: Dropouts can result in significant financial losses for the institution due to the reduction in tuition fee income.
3. **Student Welfare**: Students who dropout may face adverse long-term effects, such as limited career opportunities and lower earning potential.

Understanding and addressing the factors that lead to dropout is crucial for the institute. By identifying at-risk students early, the institute can provide targeted interventions to support these students, thereby reducing dropout rates and improving overall student outcomes.

## Project Scope

This project aims to address the issue of student dropout through the following key steps:

1. **Dropout Factor Analysis**: Identifying and analyzing factors that contribute to student dropout. This includes examining variables such as tuition fee payment status, scholarship status, and academic performance in both the 1st and 2nd semester curricular units.
2. **Business Dashboard**: Building an interactive dashboard to visualize dropout data and key factors influencing dropout rates. This dashboard will provide actionable insights for management.
3. **Dropout Prediction Model**: Developing and implementing a predictive model to identify students at risk of dropping out. This model will enable timely intervention to support at-risk students.

### Deliverables:
- **Data Analysis Report**: Detailed analysis of the factors contributing to dropout rates.
- **Interactive Dashboard**: A business dashboard insights into dropout data.
- **Predictive Model**: A machine learning model capable of predicting students at risk of dropping out.
- **Prototype Deployment**: A prototype system running locally (and later, deployed online) that demonstrates the predictive capabilities.

## Preparation

### Data Source
The data used in this project is available at the following repository: [Students Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

### Setup Environment

1. **Open Google Colab:** 
   - Go to Google Colab and create a new notebook.
   
2. **Install Libraries:**
   - Install the necessary libraries by running the following commands:
     ```python
     pip install -r requirements.txt
     ```
   - Required libraries can be found in the [requirements file](https://github.com/dimsdika12/Student-Dropout-Prediction/blob/main/requirements.txt).

## Business Dashboard

### Dashboard Overview
The business dashboard has been designed to provide comprehensive insights into factors influencing student dropout rates at Jaya Jaya Institute. It includes the following charts:
1. Proportion of Student Dropout vs. Graduation
2. Effect of Tuition Fees Payment Status on Dropout Rates
3. Impact of Scholarship Holder Status on Dropout Rates
4. Influence of Grades in 1st Semester Curricular Units on Dropout Rates
5. Influence of Grades in 2nd Semester Curricular Units on Dropout Rates

You can access the dashboard [here](https://lookerstudio.google.com/reporting/fb8428f9-eb26-485f-88fb-0bb43ef8a5a7).

## Running the Machine Learning System

### Prototype System Overview
The prototype machine learning system has been developed to predict students at risk of dropout based on historical data and identified factors. Due to current technical constraints (Streamlit being down), the prototype is currently only runnable locally.

### Access the Prototype
The prototype system can be accessed [here](https://your-prototype-link).

## Conclusion

In conclusion, the project has successfully identified several key factors influencing student dropout rates at Jaya Jaya Institute based on the analysis:
1. Based on the data, 60.85% of the students graduated and 39.15% dropped out, out of a total of 3,630 students.
2. Analysis shows that tuition fees paid up to date correlate significantly with lower dropout rates.
3. Scholarship holders exhibit lower dropout rates (134 cases) compared to non-scholarship holders (1,287 cases).
4. Higher grades in the 1st semester curricular units are associated with higher graduation rates and lower dropout probabilities.
5. Higher grades in the 2nd semester curricular units similarly correlate with higher graduation rates and lower dropout probabilities.

## Recommendation Action Items

###  Strengthen Scholarship Programs
Given the significant impact of scholarships on reducing dropout rates, prioritize expanding and promoting scholarship opportunities for eligible students.

### Implement Early Intervention Strategies
Develop and implement an early warning system using the predictive model to identify students at risk of dropout early. Provide targeted interventions such as academic counseling and support programs.

### Enhance Financial Support Services
Provide additional financial aid or flexible payment options to ensure more students can afford to pay their tuition fees on time.

### Enhance Academic Support Programs
Invest in academic support programs that focus on improving students' performance in both 1st and 2nd semester curricular units. Offer tutoring, study groups, and mentorship to help students achieve higher grades and reduce dropout rates.

These action items are tailored to address the specific findings of the analysis and aim to support Jaya Jaya Institute in effectively tackling the challenge of student dropout rates.
