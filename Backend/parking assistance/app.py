# app.py
import requests
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

GOOGLE_API_KEY = 'your_google_maps_api_key'
GOOGLE_MAPS_ENDPOINT = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

class GoogleParkingAPI(Resource):
    def get(self):
        location = request.args.get('location')
        radius = request.args.get('radius', 500)  # default radius 500 meters
        if not location:
            return {'message': 'Location parameter is required'}, 400

        params = {
            'location': location,
            'radius': radius,
            'type': 'parking',
            'key': GOOGLE_API_KEY
        }
        response = requests.get(GOOGLE_MAPS_ENDPOINT, params=params)
        return jsonify(response.json())

api.add_resource(GoogleParkingAPI, '/find_parking')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
