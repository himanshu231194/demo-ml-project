import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load data
df = pd.read_csv('data/processed/cgpa_data.csv')
x = df[['cgpa']]
y = df['package']

# Train model
model = LinearRegression()
model.fit(x, y)

# Save model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/linear_model.pkl')
print("✅ Model trained and saved to models/linear_model.pkl")