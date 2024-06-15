#!/usr/bin/env python3

from flask import Blueprint, request, jsonify, current_app

country_bp = Blueprint('country_bp', __name__)


@country_bp.route('/countries', methods=['GET'])
def get_countries():
    data_manager = current_app.config['DATA_MANAGER_COUNTRY']
    return jsonify(data_manager.data), 200


@country_bp.route('/countries/<country_code>', methods=['GET'])
def get_country_by_code(country_code):
    data_manager = current_app.config['DATA_MANAGER_COUNTRY']
    country = next(
        (c for c in data_manager.data if c['code'] == country_code.upper()), None)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country), 200


@country_bp.route('/countries/<country_code>/cities', methods=['GET'])
def get_cities_by_country_code(country_code):
    data_manager_city = current_app.config['DATA_MANAGER_CITY']
    cities = [city for city in data_manager_city.data if city['country_code']
              == country_code.upper()]
    if not cities:
        return jsonify({'error': 'No cities found for this country'}), 404
    return jsonify(cities), 200
