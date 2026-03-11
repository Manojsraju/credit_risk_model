import streamlit as st
import pandas as pd
import joblib

model = joblib.load("credit_risk_model.pkl")

st.title("Credit Risk Prediction")

age = st.number_input("Age")
sex = st.selectbox("Sex", ["male","female"])
job = st.selectbox("Job",[0,1,2,3])
housing = st.selectbox("Housing",["own","rent","free"])
saving_accounts = st.selectbox("Saving Accounts",["little","moderate","rich"])
checking_account = st.selectbox("Checking Account",["little","moderate","rich"])
credit_amount = st.number_input("Credit Amount")
duration = st.number_input("Duration")

if st.button("Predict"):
    
    data = pd.DataFrame({
        "age":[age],
        "sex":[sex],
        "job":[job],
        "housing":[housing],
        "saving_accounts":[saving_accounts],
        "checking_account":[checking_account],
        "credit_amount":[credit_amount],
        "duration":[duration]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Good Credit Risk")
    else:
        st.error("Bad Credit Risk")
