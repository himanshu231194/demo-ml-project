from flask import Flask, request, jsonify
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("simple_linear_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    cgpa = float(data['cgpa'])
    prediction = model.predict(np.array([[cgpa]]))
    return jsonify({"prediction": prediction[0]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
