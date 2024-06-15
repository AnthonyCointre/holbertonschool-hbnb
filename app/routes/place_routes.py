#!/usr/bin/env python3

from flask import Blueprint, request, jsonify, current_app
import uuid
from datetime import datetime

place_bp = Blueprint('place_bp', __name__)


@place_bp.route('/places', methods=['POST'])
def create_place():
    data_manager_place = current_app.config['DATA_MANAGER_PLACE']
    data_manager_city = current_app.config['DATA_MANAGER_CITY']
    data_manager_amenity = current_app.config['DATA_MANAGER_AMENITY']
    data = request.get_json()

    required_fields = ['name', 'description', 'address', 'city_id', 'latitude', 'longitude',
                       'host_id', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests', 'amenity_ids']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field.capitalize()} is required'}), 400

    name = data['name'].strip()
    city_id = data['city_id']
    latitude = data['latitude']
    longitude = data['longitude']
    host_id = data['host_id']
    number_of_rooms = data['number_of_rooms']
    number_of_bathrooms = data['number_of_bathrooms']
    price_per_night = data['price_per_night']
    max_guests = data['max_guests']
    amenity_ids = data['amenity_ids']

    city = next(
        (c for c in data_manager_city.data if c['id'] == city_id), None)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    amenities = [
        a for a in data_manager_amenity.data if a['id'] in amenity_ids]
    if len(amenities) != len(amenity_ids):
        return jsonify({'error': 'One or more amenities not found'}), 404

    new_place = {
        "id": str(uuid.uuid4()),
        "name": name,
        "description": data['description'],
        "address": data['address'],
        "city": city,
        "latitude": latitude,
        "longitude": longitude,
        "host_id": host_id,
        "number_of_rooms": number_of_rooms,
        "number_of_bathrooms": number_of_bathrooms,
        "price_per_night": price_per_night,
        "max_guests": max_guests,
        "amenities": amenities,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    data_manager_place.data.append(new_place)
    data_manager_place.save()

    return jsonify(new_place), 201


@place_bp.route('/places', methods=['GET'])
def get_places():
    data_manager_place = current_app.config['DATA_MANAGER_PLACE']
    return jsonify(data_manager_place.data), 200


@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    data_manager_place = current_app.config['DATA_MANAGER_PLACE']
    place = next(
        (p for p in data_manager_place.data if p['id'] == place_id), None)
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place), 200


@place_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data_manager_place = current_app.config['DATA_MANAGER_PLACE']
    data_manager_city = current_app.config['DATA_MANAGER_CITY']
    data_manager_amenity = current_app.config['DATA_MANAGER_AMENITY']
    data = request.get_json()

    place = next(
        (p for p in data_manager_place.data if p['id'] == place_id), None)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    required_fields = ['name', 'description', 'address', 'city_id', 'latitude', 'longitude',
                       'host_id', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests', 'amenity_ids']
    for field in required_fields:
        if field in data:
            if field == 'city_id':
                city = next(
                    (c for c in data_manager_city.data if c['id'] == data['city_id']), None)
                if not city:
                    return jsonify({'error': 'City not found'}), 404
                place['city'] = city
            elif field == 'amenity_ids':
                amenities = [
                    a for a in data_manager_amenity.data if a['id'] in data['amenity_ids']]
                if len(amenities) != len(data['amenity_ids']):
                    return jsonify({'error': 'One or more amenities not found'}), 404
                place['amenities'] = amenities
            else:
                place[field] = data[field]

    place['updated_at'] = datetime.now().isoformat()
    data_manager_place.save()

    return jsonify(place), 200


@place_bp.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    data_manager_place = current_app.config['DATA_MANAGER_PLACE']
    place = next(
        (p for p in data_manager_place.data if p['id'] == place_id), None)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    data_manager_place.data = [
        p for p in data_manager_place.data if p['id'] != place_id]
    data_manager_place.save()

    return '', 204
