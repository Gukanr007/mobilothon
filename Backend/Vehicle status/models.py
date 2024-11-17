# models.py
class VehicleStatus:
    def __init__(self):
        self.status = {
            "engine": {"health": "good", "message": "Engine performance is optimal."},
            "battery": {"level": 85, "health": "good", "message": "Battery level is healthy."},
            "tires": {
                "front_left": 32,
                "front_right": 32,
                "rear_left": 30,
                "rear_right": 30,
                "health": "good",
                "message": "Tire pressure is within normal range."
            }
        }

    def get_status(self):
        return self.status
