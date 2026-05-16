import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("extra_trees_credit_model.pkl")

# Load encoders
encoders = {
    "Sex": joblib.load("Sex_encoder.pkl"),
    "Housing": joblib.load("Housing_encoder.pkl"),
    "Saving accounts": joblib.load("Saving_accounts_encoder.pkl"),
    "Checking accounts": joblib.load("Checking_accounts_encoder.pkl")
}

st.title("Credit Risk Prediction Application")

st.write(
    "Enter applicant information to predict whether the credit risk is GOOD or BAD."
)

# Inputs
age = st.number_input("Age", 18, 80, 30)

sex = st.selectbox(
    "Sex",
    list(encoders["Sex"].classes_)
)

job = st.number_input(
    "Job (0-3)",
    min_value=0,
    max_value=3,
    value=1
)

housing = st.selectbox(
    "Housing",
    list(encoders["Housing"].classes_)
)

saving_accounts = st.selectbox(
    "Saving Accounts",
    list(encoders["Saving accounts"].classes_)
)

checking_accounts = st.selectbox(
    "Checking Accounts",
    list(encoders["Checking accounts"].classes_)
)

credit_amount = st.number_input(
    "Credit Amount",
    min_value=0,
    value=1000
)

duration = st.number_input(
    "Duration (months)",
    min_value=1,
    value=12
)

# Predict
if st.button("Predict Risk"):

    try:

        input_df = pd.DataFrame({
            "Age": [age],
            "Sex": [encoders["Sex"].transform([sex])[0]],
            "Job": [job],
            "Housing": [encoders["Housing"].transform([housing])[0]],
            "Saving accounts": [
                encoders["Saving accounts"].transform([saving_accounts])[0]
            ],
            "Checking accounts": [
                encoders["Checking accounts"].transform([checking_accounts])[0]
            ],
            "Credit amount": [credit_amount],
            "Duration": [duration]
        })

        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.success("The predicted credit risk is: GOOD")
        else:
            st.error("The predicted credit risk is: BAD")

    except Exception as e:
        st.error(f"Error: {e}")
