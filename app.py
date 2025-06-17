from flask import Flask, render_template, request
import os
import numpy as np
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET']) # Route to display homepage
def homepage():
    return render_template("index.html")

@app.route('/train', method=['GET']) # Route to train the pipeline
def training():
    os.system("python3 main.py")
    return "Training Successfull"

@app.route('/predict', methods=['POST', 'GET']) # Route from web UI
def index():
    if request.method == 'POST':
        try:
            pregnancies = float(request.form['pregnancies'])
            glucose = float(request.form['glucose'])
            blood_pressure = float(request.form['blood_pressure'])
            skin_thickness = float(request.form['skin_thickness'])
            insulin = float(request.form['insulin'])
            bmi = float(request.form['bmi'])
            diabetes_pedigree = float(request.form['diabetes_pedigree'])
            age = float(request.form['age'])

            data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin,
                    bmi, diabetes_pedigree, age]
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction=str(predict))
        except Exception as e:
            raise e
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)