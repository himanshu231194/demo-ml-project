import joblib
import numpy as np

# Load trained model
model = joblib.load('models/linear_model.pkl')

def predict_package(cgpa: float) -> float:
    prediction = model.predict(np.array([[cgpa]]))
    return round(prediction[0], 2)