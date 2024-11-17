# app.py
from flask_restful import Resource, Api, reqparse

# Existing imports...
from models import VehicleStatus, DriverWellness

# Initialize
vehicle_status = VehicleStatus()
driver_wellness = DriverWellness()

class WellnessAPI(Resource):
    def get(self):
        # For simplicity, we just return the current data
        return jsonify(driver_wellness.get_wellness_data())

    def post(self):
        # Set up parsing for incoming data
        parser = reqparse.RequestParser()
        parser.add_argument('heart_rate', type=int, required=True, help="Heart rate cannot be blank!")
        parser.add_argument('activity_level', type=str, required=True, help="Activity level cannot be blank!")
        args = parser.parse_args()

        # Perform check and respond
        message = driver_wellness.check_fatigue(args['heart_rate'], args['activity_level'])
        return {'message': message, 'data': driver_wellness.get_wellness_data()}

# Adding the Wellness API endpoint
api.add_resource(WellnessAPI, '/driver/wellness')

# Main app runner remains the same
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
