import pandas as pd
import numpy as np
import joblib  # To load the trained model

# Load the trained model
model_path = 'phishing_model.pkl'  # Update with your model path
grid_search = joblib.load(model_path)

# Define the feature extraction function
def extract_features(url):
    # Initialize feature values (make sure to include all features your model needs)
    qty_dot_url = url.count('.')
    qty_hyphen_url = url.count('-')
    qty_underline_url = url.count('_')
    qty_slash_url = url.count('/')
    qty_questionmark_url = url.count('?')
    qty_redirects = url.count('%')
    url_length = len(url)

    # Assuming these additional features are necessary
    asn_ip = 0  # Replace with actual extraction logic if applicable
    directory_length = 0  # Replace with actual extraction logic if applicable
    domain_google_index = 0  # Replace with actual extraction logic if applicable
    domain_in_ip = 0  # Replace with actual extraction logic if applicable
    domain_length = len(url.split('/')[2]) if len(url.split('/')) > 2 else 0

    # Create a DataFrame with the features
    features = pd.DataFrame([[qty_dot_url, qty_hyphen_url, qty_underline_url, qty_slash_url,
                               domain_length, domain_in_ip, asn_ip, qty_redirects, domain_google_index, qty_questionmark_url,  url_length,
                                directory_length]],
                            columns=['qty_dot_url', 'qty_hyphen_url', 'qty_underline_url',
                                     'qty_slash_url','domain_length','domain_in_ip','asn_ip',
                                     'qty_redirects','domain_google_index','qty_questionmark_url', 'url_length',  'directory_length'])
    return features

# Function to check if a URL is phishing
def check_phishing_url(url):
    url_features = extract_features(url)

    # Predict using the trained model
    prediction = grid_search.predict(url_features)

    return 0 if prediction[0] == 1 else 1

# Test the function with a URL
test_url = "hxxps://www.google.com/"  # Replace with a test URL
result = check_phishing_url(test_url)
print(f"The URL '{test_url}' is {result}.")
