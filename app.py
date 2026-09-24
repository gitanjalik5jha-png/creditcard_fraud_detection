import streamlit as st
import joblib
import numpy as np

model = joblib.load('fraud_detection_model.pkl')

st.title("💳 Credit Card Fraud Detection System")
st.write("Enter transaction details below to check whether it is fraudulent or legitimate.")

amount = st.number_input("Transaction Amount ($)", value=100.0)
v1 = st.number_input("V1", value=0.0)
v3 = st.number_input("V3", value=0.0)
v4 = st.number_input("V4", value=0.0)
v7 = st.number_input("V7", value=0.0)
v10 = st.number_input("V10", value=0.0)
v12 = st.number_input("V12", value=0.0)
v14 = st.number_input("V14", value=0.0)
v16 = st.number_input("V16", value=0.0)
v17 = st.number_input("V17", value=0.0)

if st.button("Check Transaction"):
    input_data = np.zeros((1, 29))
    input_data[0, -1] = amount
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("⚠️ Warning: This is a Fraudulent Transaction!")
    else:
        st.success("✅ This transaction is Legitimate (Safe).")