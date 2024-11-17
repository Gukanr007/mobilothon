# app.py
from flask_restful import Resource, Api, reqparse
from models import AmbientControlSystem

app = Flask(__name__)
api = Api(app)
ambient_control = AmbientControlSystem()

class LightingAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('color', type=str, required=True, help="Color setting is required!")
        args = parser.parse_args()
        return ambient_control.set_lighting(args['color'])

class TemperatureAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('temp', type=int, required=True, help="Temperature setting is required!")
        args = parser.parse_args()
        return ambient_control.set_temperature(args['temp'])

class AudioAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('volume', type=int, required=True, help="Volume setting is required!")
        args = parser.parse_args()
        return ambient_control.set_audio_volume(args['volume'])

api.add_resource(LightingAPI, '/ambient/lighting')
api.add_resource(TemperatureAPI, '/ambient/temperature')
api.add_resource(AudioAPI, '/ambient/audio')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
