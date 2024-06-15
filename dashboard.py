import streamlit as st
import joblib
import numpy as np

# Title
st.title("Student Dropout Prediction")

# Load model
model = joblib.load("model\logreg.joblib")

# Load scalers
scaler_tuition_fees = joblib.load("model\scaler_Tuition_fees_up_to_date.joblib")
scaler_scholarship_holder = joblib.load("model\scaler_Scholarship_holder.joblib")
scaler_curricular_units_1st_sem_approved = joblib.load("model\scaler_Curricular_units_1st_sem_approved.joblib")
scaler_curricular_units_1st_sem_grade = joblib.load("E:\project\streamlit_dash\model\scaler_Curricular_units_1st_sem_grade.joblib")
scaler_curricular_units_2nd_sem_approved = joblib.load("model\scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_curricular_units_2nd_sem_grade = joblib.load("model\scaler_Curricular_units_2nd_sem_grade.joblib")

# Input form
tuition_fees_up_to_date = st.selectbox("Tuition fees up to date", ["Yes", "No"])
scholarship_holder = st.selectbox("Scholarship holder", ["Yes", "No"])
curricular_units_1st_sem_approved = st.number_input("Curricular units 1st sem approved", min_value=0, max_value=30)
curricular_units_1st_sem_grade = st.number_input("Curricular units 1st sem grade", min_value=0, max_value=20)
curricular_units_2nd_sem_approved = st.number_input("Curricular units 2nd sem approved", min_value=0, max_value=30)
curricular_units_2nd_sem_grade = st.number_input("Curricular units 2nd sem grade", min_value=0, max_value=20)

# Tombol untuk prediksi
if st.button("Predict"):
    # Konversi data kategorikal
    tuition_fees_up_to_date_encoded = 1 if tuition_fees_up_to_date == "Yes" else 0
    scholarship_holder_encoded = 1 if scholarship_holder == "Yes" else 0

    # Gabungkan data input sebelum scaling
    input_data = np.array([
        tuition_fees_up_to_date_encoded,
        scholarship_holder_encoded,
        curricular_units_1st_sem_approved,
        curricular_units_1st_sem_grade,
        curricular_units_2nd_sem_approved,
        curricular_units_2nd_sem_grade,
    ]).reshape(1, -1)

    # Scaling data numerik satu per satu dan cek hasil scaling
    tuition_fees_scaled = scaler_tuition_fees.transform([[input_data[0, 0]]])[0, 0]
    scholarship_holder_scaled = scaler_scholarship_holder.transform([[input_data[0, 1]]])[0, 0]
    curricular_units_1st_sem_approved_scaled = scaler_curricular_units_1st_sem_approved.transform([[input_data[0, 2]]])[0, 0]
    curricular_units_1st_sem_grade_scaled = scaler_curricular_units_1st_sem_grade.transform([[input_data[0, 3]]])[0, 0]
    curricular_units_2nd_sem_approved_scaled = scaler_curricular_units_2nd_sem_approved.transform([[input_data[0, 4]]])[0, 0]
    curricular_units_2nd_sem_grade_scaled = scaler_curricular_units_2nd_sem_grade.transform([[input_data[0, 5]]])[0, 0]

    # Output nilai hasil scaling untuk pengecekan
    # st.write(f"Scaled values:\n"
    #          f"Tuition Fees Up To Date: {tuition_fees_scaled}\n"
    #          f"Scholarship Holder: {scholarship_holder_scaled}\n"
    #          f"Curricular Units 1st Sem Approved: {curricular_units_1st_sem_approved_scaled}\n"
    #          f"Curricular Units 1st Sem Grade: {curricular_units_1st_sem_grade_scaled}\n"
    #          f"Curricular Units 2nd Sem Approved: {curricular_units_2nd_sem_approved_scaled}\n"
    #          f"Curricular Units 2nd Sem Grade: {curricular_units_2nd_sem_grade_scaled}")

    # Gabungkan kembali data yang telah di-scale
    input_data_scaled = np.array([
        tuition_fees_scaled,
        scholarship_holder_scaled,
        curricular_units_1st_sem_approved_scaled,
        curricular_units_1st_sem_grade_scaled,
        curricular_units_2nd_sem_approved_scaled,
        curricular_units_2nd_sem_grade_scaled,
    ]).reshape(1, -1)

    # Prediksi
    prediction = model.predict(input_data_scaled)

    # Output
    if prediction == 0:
        st.write("Student is  expected to Dropout.")
    else:
        st.write("Student is Not expected to Dropout.")

