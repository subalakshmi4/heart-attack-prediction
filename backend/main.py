from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np


# Create FastAPI application
app = FastAPI()


# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load the trained Random Forest pipeline
model = joblib.load(
    "backend/random_forest_pipeline.joblib"
)


# Define the data received from the frontend
class PatientData(BaseModel):
    age: float
    gender: float
    heart_rate: float
    systolic_blood_pressure: float
    diastolic_blood_pressure: float
    blood_sugar: float
    ck_mb: float
    troponin: float


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Heart Attack Prediction API is running!"
    }


# Prediction endpoint
@app.post("/predict")
def predict(data: PatientData):

    # Arrange the input values in the same order
    # used when training the model
    features = np.array([[
        data.age,
        data.gender,
        data.heart_rate,
        data.systolic_blood_pressure,
        data.diastolic_blood_pressure,
        data.blood_sugar,
        data.ck_mb,
        data.troponin
    ]])

    # Make prediction
    prediction = model.predict(features)[0]

    # Convert prediction into readable text
    if prediction == 1:
        result = "Positive Prediction"
    else:
        result = "Negative Prediction"

    return {
        "prediction": result
    }

