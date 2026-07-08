import streamlit as st
import joblib
import numpy as np

model = joblib.load('fraud_detection_model.pkl')

st.title("AI-Based Banking Fraud Detection System")

st.write("Enter transaction details to predict fraud or genuine transaction.")

time = st.number_input("Enter Time")
v1 = st.number_input("Enter V1")
v2 = st.number_input("Enter V2")
v3 = st.number_input("Enter V3")
v4 = st.number_input("Enter V4")
v5 = st.number_input("Enter V5")
v6 = st.number_input("Enter V6")
v7 = st.number_input("Enter V7")
v8 = st.number_input("Enter V8")
v9 = st.number_input("Enter V9")
v10 = st.number_input("Enter V10")
v11 = st.number_input("Enter V11")
v12 = st.number_input("Enter V12")
v13 = st.number_input("Enter V13")
v14 = st.number_input("Enter V14")
v15 = st.number_input("Enter V15")
v16 = st.number_input("Enter V16")
v17 = st.number_input("Enter V17")
v18 = st.number_input("Enter V18")
v19 = st.number_input("Enter V19")
v20 = st.number_input("Enter V20")
v21 = st.number_input("Enter V21")
v22 = st.number_input("Enter V22")
v23 = st.number_input("Enter V23")
v24 = st.number_input("Enter V24")
v25 = st.number_input("Enter V25")
v26 = st.number_input("Enter V26")
v27 = st.number_input("Enter V27")
v28 = st.number_input("Enter V28")
amount = st.number_input("Enter Amount")

if st.button("Predict Transaction"):

    input_data = np.array([[
        time, v1, v2, v3, v4, v5, v6, v7, v8,
        v9, v10, v11, v12, v13, v14, v15,
        v16, v17, v18, v19, v20, v21,
        v22, v23, v24, v25, v26, v27,
        v28, amount
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success("Genuine Transaction")
    else:
        st.error("Fraud Transaction")