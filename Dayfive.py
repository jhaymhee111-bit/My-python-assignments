import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
#  Synthetic clinical diagnostic records
X = np.array([
    [22, 36.5], [45, 38.8], [31, 37.1], [58, 39.5],
    [29, 36.8], [62, 38.9], [35, 37.5], [51, 39.1]
])  #  Features: [Age, Temperature]
#  Target: [0 = Low Risk, 1 = High Risk]
y = np.array([0, 1, 0, 1, 0, 1, 0, 1])
#  1. Train-test partition
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
#  2. Feature Standardization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
#  3. Model Training & Evaluation
clf = LogisticRegression()
clf.fit(X_train_scaled, y_train)
predictions = clf.predict(X_test_scaled)
print(
    f"Test Classification Accuracy: {accuracy_score(y_test, predictions):.2%}")
