# models.py

class DriverWellness:
    def __init__(self):
        # Simulate some initial data
        self.data = {
            "heart_rate": 72,  # Average resting heart rate
            "activity_level": "moderate",  # Simulated based on the user's driving activity
            "fatigue_level": "alert"  # Initial state
        }

    def check_fatigue(self, heart_rate, activity_level):
        # Simplified logic to determine fatigue
        if heart_rate > 100 and activity_level == 'low':
            self.data['fatigue_level'] = 'high'
            return "Fatigue detected: Please take a rest."
        else:
            self.data['fatigue_level'] = 'alert'
            return "Driver condition is normal."

    def get_wellness_data(self):
        return self.data
