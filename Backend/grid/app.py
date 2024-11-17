# app.py
from flask import Flask
from flask_restful import Resource, Api, reqparse
from models import EnergyManagementSystem

app = Flask(__name__)
api = Api(app)
energy_system = EnergyManagementSystem()

class EnergyAPI(Resource):
    def get(self):
        # Return current battery status
        battery_status = energy_system.get_battery_status()
        return {'battery_level': battery_status}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('energy_to_share', type=int, required=True, help="Energy to share percentage is required!")
        args = parser.parse_args()

        message = energy_system.manage_energy_sharing(args['energy_to_share'])
        return {'message': message}

api.add_resource(EnergyAPI, '/manage-energy')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
