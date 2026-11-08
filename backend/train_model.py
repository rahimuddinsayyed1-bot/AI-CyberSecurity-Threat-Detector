import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

data = {
    'packets': [100, 200, 5000, 7000, 120, 300],
    'failed_logins': [1, 0, 50, 80, 1, 2],
    'malware_detected': [0, 0, 1, 1, 0, 0],
    'threat': [0, 0, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

X = df[['packets', 'failed_logins', 'malware_detected']]
y = df['threat']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

import os
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
joblib.dump(model, model_path)

print("AI Model Trained Successfully")