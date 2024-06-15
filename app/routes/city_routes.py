#!/usr/bin/env python3

from flask import Blueprint, request, jsonify, current_app
import uuid
from datetime import datetime

city_bp = Blueprint('city_bp', __name__)


@city_bp.route('/cities', methods=['POST'])
def create_city():
    data_manager_city = current_app.config['DATA_MANAGER_CITY']
    data_manager_country = current_app.config['DATA_MANAGER_COUNTRY']
    data = request.get_json()

    if not data or not data.get('name') or not data.get('country_code'):
        return jsonify({'error': 'Name and country_code are required'}), 400

    country_code = data['country_code'].upper()
    if not any(country['code'] == country_code for country in data_manager_country.data):
        return jsonify({'error': 'Invalid country code'}), 400

    if any(city['name'].lower() == data['name'].lower() and city['country_code'] == country_code for city in data_manager_city.data):
        return jsonify({'error': 'City already exists in this country'}), 409

    new_city = {
        "id": str(uuid.uuid4()),
        "name": data['name'],
        "country_code": country_code,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    data_manager_city.data.append(new_city)
    data_manager_city.save()

    return jsonify(new_city), 201


@city_bp.route('/cities', methods=['GET'])
def get_cities():
    data_manager = current_app.config['DATA_MANAGER_CITY']
    return jsonify(data_manager.data), 200


@city_bp.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    data_manager = current_app.config['DATA_MANAGER_CITY']
    city = next((c for c in data_manager.data if c['id'] == city_id), None)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city), 200


@city_bp.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    data_manager_city = current_app.config['DATA_MANAGER_CITY']
    data_manager_country = current_app.config['DATA_MANAGER_COUNTRY']
    data = request.get_json()

    city = next(
        (c for c in data_manager_city.data if c['id'] == city_id), None)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    if 'name' in data:
        city['name'] = data['name']
    if 'country_code' in data:
        country_code = data['country_code'].upper()
        if not any(country['code'] == country_code for country in data_manager_country.data):
            return jsonify({'error': 'Invalid country code'}), 400
        city['country_code'] = country_code

    city['updated_at'] = datetime.now().isoformat()
    data_manager_city.save()

    return jsonify(city), 200


@city_bp.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    data_manager = current_app.config['DATA_MANAGER_CITY']
    city = next((c for c in data_manager.data if c['id'] == city_id), None)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    data_manager.data = [c for c in data_manager.data if c['id'] != city_id]
    data_manager.save()

    return '', 204
