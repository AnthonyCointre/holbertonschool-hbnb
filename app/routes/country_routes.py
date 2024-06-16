#!/usr/bin/env python3

from flask import Blueprint, jsonify, request, abort, current_app
from datetime import datetime
from app.models.country import Country

country_bp = Blueprint('country', __name__)


@country_bp.route('/countries', methods=['GET'])
def get_countries():
    data_manager = current_app.config['DATA_MANAGER_COUNTRIES']
    countries = [country.to_dict()
                 for country in
                 data_manager.storage.get('Country', {}).values()]
    return jsonify(countries), 200


@country_bp.route('/countries/<country_code>', methods=['GET'])
def get_country_code(country_code):
    data_manager = current_app.config['DATA_MANAGER_COUNTRIES']
    country = data_manager.get_country_by_code(country_code)
    if country is None:
        abort(404, 'Country not found.')
    return jsonify(country.to_dict()), 200


@country_bp.route('/countries/<country_code>/cities', methods=['GET'])
def get_city_by_country_code(country_code):

    data_manager = current_app.config['DATA_MANAGER_CITIES']
    cities = []
    for city in data_manager.storage.get('City', {}).values():
        if city.country_id == country_code:
            cities.append(city.to_dict())
    if not cities:
        abort(404, f'No cities found for country code {country_code}.')
    return jsonify(cities), 200
