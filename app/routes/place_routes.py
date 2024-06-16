#!/usr/bin/env python3

from flask import Blueprint, jsonify, request, abort, current_app
from datetime import datetime
from app.models.place import Place

place_bp = Blueprint('place', __name__)


@place_bp.route('/places', methods=['POST'])
def create_place():

    data_manager = current_app.config['DATA_MANAGER_PLACES']
    if not request.json:
        abort(400, 'Input data cannot empty.')
    name = request.json.get('name')
    description = request.json.get('description')
    address = request.json.get('address')
    city_id = request.json.get('city_id')
    try:
        latitude = float(request.json.get('latitude'))
        longitude = float(request.json.get('longitude'))
        host_id = request.json.get('host_id')
        num_rooms = int(request.json.get('num_rooms'))
        num_bathrooms = int(request.json.get('num_bathrooms'))
        price_per_night = float(request.json.get('price_per_night'))
        max_guests = int(request.json.get('max_guests'))
    except ValueError as e:
        abort(400, str(e))
    amenities = request.json.get('amenities', [])
    if not all([name, address, city_id, host_id, num_rooms, num_bathrooms,
                price_per_night, max_guests]):
        abort(400, 'Missing fields.')
    try:
        place = Place(name, description, address, city_id, latitude,
                      longitude,
                      host_id, num_rooms, num_bathrooms, price_per_night,
                      max_guests, amenities, data_manager)
    except ValueError as e:
        abort(400, str(e))
    data_manager.save(place)
    return jsonify(place.to_dict()), 201


@place_bp.route('/places', methods=['GET'])
def get_places():
    data_manager = current_app.config['DATA_MANAGER_PLACES']
    place_objects = data_manager.storage.get('Place', {}).values()
    places = []
    for place in place_objects:
        place_dict = place.to_dict()
        city = data_manager.get(place_dict['city_id'], 'City')
        place_dict['city'] = city.to_dict() if city else None
        amenities = [data_manager.get(amenity_id, 'Amenity').to_dict(
        ) for amenity_id in place_dict['amenities'] if
            data_manager.get(amenity_id, 'Amenity')]
        place_dict['amenities'] = amenities
        places.append(place_dict)
    return jsonify(places), 200


@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    data_manager = current_app.config['DATA_MANAGER_PLACES']
    place = data_manager.get(place_id, 'Place')
    if place is None:
        abort(404, 'Place not found.')
    place_dict = place.to_dict()
    city = data_manager.get(place_dict['city_id'], 'City')
    place_dict['city'] = city.to_dict() if city else None
    amenities = [data_manager.get(amenity_id, 'Amenity').to_dict(
    ) for amenity_id in place_dict['amenities'] if
        data_manager.get(amenity_id, 'Amenity')]
    place_dict['amenities'] = amenities
    return jsonify(place_dict), 200


@place_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data_manager = current_app.config['DATA_MANAGER_PLACES']
    place = data_manager.get(place_id, 'Place')
    if place is None:
        abort(404, 'Place not found.')
    data = request.get_json()
    if not data:
        abort(400, 'Input data cannot be empty.')
    try:
        for key, value in data.items():
            if hasattr(place, key):
                if not value:
                    abort(400, f"{key} cannot be empty.")
                setattr(place, key, value)
        place.updated_at = datetime.utcnow()
        data_manager.save(place)
    except ValueError as e:
        abort(400, str(e))
    return jsonify(place.to_dict()), 200


@place_bp.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    data_manager = current_app.config['DATA_MANAGER_PLACES']
    place = data_manager.get(place_id, 'Place')
    if place is None:
        abort(404, 'Place not found.')
    data_manager.delete(place_id, 'Place')
    return '', 204
