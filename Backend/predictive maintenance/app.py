# app.py
from flask_restful import Resource, Api, reqparse
from models import PredictiveMaintenanceModel

app = Flask(__name__)
api = Api(app)
maintenance_model = PredictiveMaintenanceModel()

class MaintenancePredictionAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('mileage', type=int, required=True, help="Mileage cannot be blank!")
        parser.add_argument('age', type=int, required=True, help="Age of vehicle cannot be blank!")
        parser.add_argument('average_rpm', type=int, required=True, help="Average RPM cannot be blank!")
        parser.add_argument('number_of_alerts', type=int, required=True, help="Number of alerts cannot be blank!")
        args = parser.parse_args()

        prediction = maintenance_model.predict_maintenance(
            args['mileage'],
            args['age'],
            args['average_rpm'],
            args['number_of_alerts']
        )
        return {'days_until_next_maintenance': prediction}

api.add_resource(MaintenancePredictionAPI, '/predict-maintenance')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
