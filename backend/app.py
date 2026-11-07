from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import random
import joblib

app = Flask(__name__)
CORS(app)

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
if not os.path.exists(model_path):
    model_path = 'model.pkl'
model = joblib.load(model_path)

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

    data = request.json or {}

    packets = data.get('packets', 150)
    failed_logins = data.get('failed_logins', 0)
    malware_detected = data.get('malware_detected', 0)

    prediction = model.predict([
        [packets, failed_logins, malware_detected]
    ])

    is_threat = True if int(prediction[0]) == 1 else False
    result = "Threat Detected" if is_threat else "Safe"
    score = int(random.randint(68, 97) if is_threat else random.randint(8, 32))

    return jsonify({
        "prediction": result,
        "score": score,
        "is_threat": is_threat,
        "packets": int(packets),
        "failed_logins": int(failed_logins),
        "malware_detected": int(malware_detected)
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