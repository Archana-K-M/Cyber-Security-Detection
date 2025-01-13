from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
import joblib
import sys
import os
import phishing_detection as ph
import malware_detection as md
#sys.path.append(os.path.join(os.getcwd(), 'Phishing_Model'))

app = Flask(__name__)

# Load models
malware_model = pickle.load(open('trained_model.pkl', 'rb'))
phishing_model = pickle.load(open('phishing_model.pkl', 'rb'))
#dos_model = pickle.load(open('C:/Users/User/Desktop/Hackfest/DoS_Model/multiclass_attack_model_nslkdd.pkl', 'rb'))

# Home route with links to different models
@app.route('/')
def home():
    return render_template('index.html')

# Route for malware detection
@app.route('/malware', methods=['GET', 'POST'])
def malware():
    if request.method == 'POST':
        url = request.form['url']
        prediction = md.test_url(url)
        result = "Malware Detected. Files quarantined" if prediction == 1 else "No Malware Detected"
        return render_template('malware.html', prediction_text=result)
    return render_template('malware.html')

# Route for phishing detection
@app.route('/phishing', methods=['GET', 'POST'])
def phishing():
    if request.method == 'POST':
        # Example: process phishing detection
        url = request.form['url']
        prediction = ph.check_phishing_url(url)
        result = "Phishing Detected\nFiles quarantined" if prediction == 0 else "No Phishing Detected"
        return render_template('phishing.html', prediction_text=result)
    return render_template('phishing.html')

# Route for DoS detection
@app.route('/dos', methods=['GET', 'POST'])
def dos():
    if request.method == 'POST':
        # Example: process DoS attack detection
        features = [float(x) for x in request.form.values()]
        features = np.array(features).reshape(1, -1)
        prediction = dos_model.predict(features)
        result = "DoS Attack Detected" if prediction[0] == 1 else "No DoS Attack Detected"
        return render_template('dos.html', prediction_text=result)
    return render_template('dos.html')

if __name__ == "__main__":
    app.run(debug=True)

