from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load('model.pkl')

# Dashboard Statistics
@app.route('/stats')
def stats():

    return jsonify({
        "totalThreats": 1248,
        "activeAlerts": 23,
        "blockedAttacks": 942,
        "vulnerabilities": 17
    })


# Threat Prediction API
@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    packets = data['packets']
    failed_logins = data['failed_logins']
    malware_detected = data['malware_detected']

    prediction = model.predict([
        [packets, failed_logins, malware_detected]
    ])

    result = "Threat Detected" if prediction[0] == 1 else "Safe"

    return jsonify({
        "prediction": result
    })


# Live Traffic API
@app.route('/traffic')
def traffic():

    return jsonify({
        "incoming": random.randint(200, 900),
        "outgoing": random.randint(100, 700)
    })


# Alerts API
@app.route('/alerts')
def alerts():

    data = [
        {
            "type": "Malware",
            "severity": "High",
            "source": "192.168.1.45"
        },
        {
            "type": "Phishing",
            "severity": "Medium",
            "source": "mail.fake.com"
        },
        {
            "type": "DDoS",
            "severity": "Critical",
            "source": "45.76.12.8"
        }
    ]

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)