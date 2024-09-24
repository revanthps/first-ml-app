# app.py
from fastapi import FastAPI
import pickle
from pydantic import BaseModel

# Load the pre-trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()

# Define a request body using Pydantic
class UserData(BaseModel):
    age: int
    income: float

# Prediction route
@app.post("/predict")
def predict(data: UserData):
    input_data = [[data.age, data.income]]
    prediction = model.predict(input_data)
    result = "Coffee" if prediction[0] == 1 else "Tea"
    return {"prediction": result}
