#!/usr/bin/env python3

from flask import Blueprint, request, jsonify, current_app
import uuid
from datetime import datetime

amenity_bp = Blueprint('amenity_bp', __name__)


@amenity_bp.route('/amenities', methods=['POST'])
def create_amenity():
    data_manager = current_app.config['DATA_MANAGER_AMENITY']
    data = request.get_json()

    if not data or not data.get('name'):
        return jsonify({'error': 'Name is required'}), 400

    name = data['name'].strip()
    if any(amenity['name'].lower() == name.lower() for amenity in data_manager.data):
        return jsonify({'error': 'Amenity already exists'}), 409

    new_amenity = {
        "id": str(uuid.uuid4()),
        "name": name,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    data_manager.data.append(new_amenity)
    data_manager.save()

    return jsonify(new_amenity), 201


@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    data_manager = current_app.config['DATA_MANAGER_AMENITY']
    return jsonify(data_manager.data), 200


@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    data_manager = current_app.config['DATA_MANAGER_AMENITY']
    amenity = next(
        (a for a in data_manager.data if a['id'] == amenity_id), None)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity), 200


@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data_manager = current_app.config['DATA_MANAGER_AMENITY']
    data = request.get_json()

    amenity = next(
        (a for a in data_manager.data if a['id'] == amenity_id), None)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404

    if 'name' in data:
        name = data['name'].strip()
        if any(a['name'].lower() == name.lower() and a['id'] != amenity_id for a in data_manager.data):
            return jsonify({'error': 'Amenity name already exists'}), 409
        amenity['name'] = name

    amenity['updated_at'] = datetime.now().isoformat()
    data_manager.save()

    return jsonify(amenity), 200


@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    data_manager = current_app.config['DATA_MANAGER_AMENITY']
    amenity = next(
        (a for a in data_manager.data if a['id'] == amenity_id), None)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404

    data_manager.data = [a for a in data_manager.data if a['id'] != amenity_id]
    data_manager.save()

    return '', 204
