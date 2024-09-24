# streamlit_app.py
import streamlit as st
import requests

st.title("ML Prediction App")

# Input fields for user data
age = st.number_input("Age", min_value=18, max_value=100, value=25)
income = st.number_input("Income", min_value=0, value=50000)

# Button to trigger the prediction
if st.button("Get Prediction"):
    input_data = {"age": age, "income": income}
    
    # Send data to FastAPI backend
    response = requests.post("https://first-ml-app.onrender.com/predict", json=input_data)
    
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.write(f"Prediction: {prediction}")
    else:
        st.write("Error in getting prediction")
