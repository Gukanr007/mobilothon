# app.py
from flask import Flask, jsonify
from models import VehicleStatus
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
vehicle_status = VehicleStatus()

class StatusAPI(Resource):
    def get(self):
        return jsonify(vehicle_status.get_status())

api.add_resource(StatusAPI, '/vehicle/status')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
