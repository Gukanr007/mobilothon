# models.py
class AccidentDetectionSystem:
    def analyze_sensor_data(self, acceleration):
        # Simulating accident detection based on sudden deceleration
        if acceleration < -2.5:  # Threshold for detecting a crash (e.g., sudden stop)
            return True
        return False
