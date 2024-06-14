#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Place API',
          description='API for managing places')

places = []

place_model = api.model('Place', {
    'id': fields.String(readOnly=True, description='The unique identifier of a place'),
    'name': fields.String(required=True, description='Place name'),
    'description': fields.String(description='Place description'),
    'address': fields.String(required=True, description='Place address'),
    'city_id': fields.String(required=True, description='City ID'),
    'latitude': fields.Float(description='Latitude of the place'),
    'longitude': fields.Float(description='Longitude of the place'),
    'host_id': fields.String(description='Host ID'),
    'number_of_rooms': fields.Integer(description='Number of rooms'),
    'number_of_bathrooms': fields.Integer(description='Number of bathrooms'),
    'price_per_night': fields.Float(description='Price per night'),
    'max_guests': fields.Integer(description='Maximum number of guests'),
    'amenity_ids': fields.List(fields.String, description='List of amenity IDs')
})

@app.route('/places/', methods=['POST'])
def create_place():
    data = request.json
    new_place = {
        'id': str(len(places) + 1),
        'name': data['name'],
        'description': data.get('description', ''),
        'address': data['address'],
        'city_id': data['city_id'],
        'latitude': data.get('latitude', 0.0),
        'longitude': data.get('longitude', 0.0),
        'host_id': data.get('host_id', ''),
        'number_of_rooms': data.get('number_of_rooms', 0),
        'number_of_bathrooms': data.get('number_of_bathrooms', 0),
        'price_per_night': data.get('price_per_night', 0.0),
        'max_guests': data.get('max_guests', 0),
        'amenity_ids': data.get('amenity_ids', [])
    }
    places.append(new_place)
    return jsonify(new_place), 201
