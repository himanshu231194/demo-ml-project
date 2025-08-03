from flask import Flask, request, jsonify
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from predict import predict_package

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    cgpa = data.get('cgpa')
    if cgpa is None:
        return jsonify({'error': 'Please provide CGPA'}), 400
    
    result = predict_package(float(cgpa))
    return jsonify({'cgpa': cgpa, 'predicted_package_lpa': result})

if __name__ == '__main__':
    app.run(debug=True)