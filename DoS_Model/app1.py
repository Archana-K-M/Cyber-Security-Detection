from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
import joblib
import sys
import os
import phishing_detection as ph
import malware_detection as md
rf_model = joblib.load('dos_model_nslkdd.pkl')  # Path to your trained model
scaler = joblib.load('scaler.pkl')
#sys.path.append(os.path.join(os.getcwd(), 'Phishing_Model'))

app = Flask(__name__)

# Load models
malware_model = pickle.load(open('C:/Users/User/Desktop/Hackfest/Malware_Model/trained_model.pkl', 'rb'))
phishing_model = pickle.load(open('C:/Users/User/Desktop/Hackfest/Phishing_Model/phishing_model.pkl', 'rb'))
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
        result = "Malware Detected" if prediction == 1 else "No Malware Detected"
        return render_template('malware.html', prediction_text=result)
    return render_template('malware.html')

# Route for phishing detection
@app.route('/phishing', methods=['GET', 'POST'])
def phishing():
    if request.method == 'POST':
        # Example: process phishing detection
        url = request.form['url']
        prediction = ph.check_phishing_url(url)
        result = "Phishing Detected" if prediction == 0 else "No Phishing Detected"
        return render_template('phishing.html', prediction_text=result)
    return render_template('phishing.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Expecting a JSON input
    # Extract features from JSON input
    features = [
        data['duration'],
        data['protocol_type'],
        data['service'],
        data['flag'],
        data['src_bytes'],
        data['dst_bytes'],
        data['land'],
        data['wrong_fragment'],
        data['urgent'],
        data['hot'],
        data['num_failed_logins'],
        data['logged_in'],
        data['num_compromised'],
        data['root_shell'],
        data['su_attempted'],
        data['num_root'],
        data['num_file_creations'],
        data['num_shells'],
        data['num_access_files'],
        data['num_outbound_cmds'],
        data['is_host_login'],
        data['is_guest_login'],
        data['count'],
        data['srv_count'],
        data['serror_rate'],
        data['srv_serror_rate'],
        data['rerror_rate'],
        data['srv_rerror_rate'],
        data['same_srv_rate'],
        data['diff_srv_rate'],
        data['srv_diff_host_rate'],
        data['dst_host_count'],
        data['dst_host_srv_count'],
        data['dst_host_same_srv_rate'],
        data['dst_host_diff_srv_rate'],
        data['dst_host_same_src_port_rate'],
        data['dst_host_srv_diff_host_rate'],
        data['dst_host_serror_rate'],
        data['dst_host_srv_serror_rate'],
        data['dst_host_rerror_rate'],
        data['dst_host_srv_rerror_rate'],
    ]
    
    # Convert to numpy array for scaling
    features_scaled = scaler.transform(np.array([features]))
    
    # Make prediction
    prediction = rf_model.predict(features_scaled)
    
    # Prepare response
    result = "DoS Attack Detected" if prediction[0] == 1 else "No Attack"
    
    return jsonify({'result': result})



if __name__ == "__main__":
    app.run(debug=True)

