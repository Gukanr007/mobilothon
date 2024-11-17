# models.py
from sklearn.linear_model import LinearRegression
import numpy as np

class PredictiveMaintenanceModel:
    def __init__(self):
        # Simulated training data
        # Features: Mileage, Age of Vehicle, Average RPM, Number of Alerts
        # Target: Days until next maintenance
        X = np.array([[10000, 3, 600, 2], [50000, 5, 700, 10], [30000, 4, 650, 5]])
        y = np.array([180, 30, 90])
        self.model = LinearRegression()
        self.model.fit(X, y)

    def predict_maintenance(self, mileage, age, average_rpm, number_of_alerts):
        X_new = np.array([[mileage, age, average_rpm, number_of_alerts]])
        return self.model.predict(X_new)[0]
