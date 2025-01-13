# Cyber-Security-Detection
## CyberFind (Team Archons)

The **Cybersecurity Detection System** is a web-based application designed to identify and detect common cyber threats, including:
- **Malware Detection**
- **Phishing Detection**
- **DoS Attack Detection**

This tool helps users analyze suspicious URLs and provides insights into potential threats.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Screenshots](#screenshots)
6. [Contributors](#contributors)
7. [Contact](#contact)

---
## Features
- **Malware Detection**: Identify harmful software that may compromise systems.
- **Phishing Detection**: Detect fraudulent attempts to steal sensitive information via malicious websites.
- **DoS Attack Detection**: Recognize potential denial-of-service attack patterns.
- **Interactive UI**: Simple and intuitive interface for threat analysis.
- **Real-time Predictions**: Uses pre-trained machine learning models for fast and accurate detection.

---

## Technologies Used
### Frontend:
- **HTML5**, **CSS3**: Responsive design for all pages.

### Backend:
- **Flask**: Python web framework for API endpoints.
- **Python**: Core logic for detection models and backend processing.

### Machine Learning:
- **Scikit-learn**: Model training and inference.
- **Joblib**: Serialization and deserialization of machine learning models.
- **Logistic Regression**: Used for detection.

---

## Installation
### Prerequisites
- Python 3.x
- Install the pakages.
   ```bash
   pip install flask joblib scikit-learn jinja2 werkzeug numpy pandas matplotlib seaborn gunicorn
   
### Steps to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Archana-K-M/Cyber-Security-Detection.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Cyber-Security-Detection
   ```
3. Set up a virtual environment:(optional if environment is set already)
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   flask run
   ```
6. Open your browser and visit `http://127.0.0.1:5000`.
   
---

## Usage
- The system helps detect potential **malware** in URLs, protecting users from harmful software.  
- It identifies **phishing attempts**, preventing users from falling victim to fraudulent websites designed to steal sensitive information.  
- The system can detect **Denial of Service (DoS) attacks**, which aim to disrupt services by overwhelming them with traffic.  
- It provides real-time security insights, helping users quickly identify and mitigate cyber threats.

---

## Screenshots

---

## Contributors
We thank the following people for their contributions to this project:

- **Archana K M** - (https://github.com/Archana-K-M)
- **Anirudhh S** - (https://github.com/rudhhstoic)
- **Varsha G** - (https://github.com/Varshavishnu)
Contributions are welcome! Feel free to fork the repository and submit pull requests.
---

## Contact
For any inquiries or feedback, reach out to:

- **Archana K M**
- **Email**: archanakm297@gmail.com
- **GitHub**: (https://github.com/Archana-K-M)
---


