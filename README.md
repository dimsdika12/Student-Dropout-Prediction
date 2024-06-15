# Student Dropout Prediction

## Business Understanding

### Business Background
Jaya Jaya Institute is an established educational institution that has been operating since 2000. Over the years, it has produced numerous graduates with a strong reputation. However, the institute faces a significant issue of high dropout rates among its students. This not only tarnishes the institution's reputation but also negatively impacts students who fail to complete their education.

### Business Problem
The main challenge faced by Jaya Jaya Institute is the high number of students who do not complete their education, commonly referred to as dropout. Some of the key business problems to be addressed include:
1. Identifying the factors contributing to student dropout.
2. Developing a predictive model to detect students at risk of dropping out.
3. Building a business dashboard that provides comprehensive insights into the dropout situation at Jaya Jaya Institute.

## Project Scope
This project will encompass several key steps:
1. **Dropout Factor Analysis**: Identifying and analyzing factors that contribute to student dropout.
2. **Business Dashboard**: Building a dashboard to visualize real-time dropout data for management.
3. **Dropout Prediction Model**: Developing and implementing a model to predict students likely to dropout, enabling timely intervention.

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
The prototype system can be accessed [here](https://your-prototype-link). I will update in here

## Conclusion

In conclusion, the project has successfully identified several key factors influencing student dropout rates at Jaya Jaya Institute based on the analysis:
1. Based on the data, 60.85% of the students graduated and 39.15% dropped out, out of a total of 3,630 students.
2. Analysis shows that tuition fees paid up to date (Yes) correlate significantly with higher dropout rates.
   - Tuition Fees up to Date (No): There were 457 cases of student dropout.
   - Tuition Fees up to Date (Yes): There were 964 cases of student dropout.
4. Scholarship holders exhibit lower dropout rates (134 cases) compared to non-scholarship holders (1,287 cases).
5. Higher grades in both the 1st and 2nd semester curricular units are associated with higher graduation rates and lower dropout probabilities.

## Recommendation Action Items

### Strengthen Scholarship Programs
Given the significant impact of scholarships on reducing dropout rates, prioritize expanding and promoting scholarship opportunities for eligible students.

### Enhance Financial Support Services
Provide additional financial aid or flexible payment options to ensure more students can afford to pay their tuition fees on time.

### Implement Early Intervention Strategies
Develop and implement an early warning system using the predictive model to identify students at risk of dropout early. Provide targeted interventions such as academic counseling and support programs.

These action items are tailored to address the specific findings of the analysis and aim to support Jaya Jaya Institute in effectively tackling the challenge of student dropout rates.

  
