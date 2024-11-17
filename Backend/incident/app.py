# app.py
from flask_restful import Resource, Api, reqparse
from models import AccidentDetectionSystem

app = Flask(__name__)
api = Api(app)
accident_detector = AccidentDetectionSystem()

class AccidentAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('acceleration', type=float, required=True, help="Acceleration data is required!")
        args = parser.parse_args()

        accident_detected = accident_detector.analyze_sensor_data(args['acceleration'])
        if accident_detected:
            return {'accident': True, 'message': 'Accident detected, emergency services notified.'}
        return {'accident': False, 'message': 'No accident detected.'}

api.add_resource(AccidentAPI, '/detect-accident')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
