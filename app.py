import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Approval Prediction")

income = st.number_input("Income")
cibil = st.number_input("CIBIL Score")
loan_amount = st.number_input("Loan Amount")
assets = st.number_input("Assets Value")

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

# Encoding
education = 1 if education=="Graduate" else 0
self_employed = 1 if self_employed=="Yes" else 0

if st.button("Predict"):

    data = np.array([[income,
                      cibil,
                      loan_amount,
                      assets,
                      education,
                      self_employed]])

    prediction = model.predict(data)

    if prediction[0]==1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")