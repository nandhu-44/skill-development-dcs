from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

model_path = 'models/diabetes_model.pkl'

if not os.path.exists(model_path):
    raise FileNotFoundError("Model file not found. Please train the model first by running train.py.")

model = joblib.load(model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        pregnancies = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bloodpressure = int(request.form['bloodpressure'])
        bmi = float(request.form['bmi'])
        age = int(request.form['age'])

        input_data = pd.DataFrame([[pregnancies, glucose, bloodpressure, bmi, age]],
                                  columns=["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"])
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        confidence = np.max(probabilities) * 100
        
        result = "Diabetic" if int(prediction) == 1 else "Not Diabetic"
        return jsonify({'prediction': result, 'confidence': round(confidence, 2)})

    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=False)