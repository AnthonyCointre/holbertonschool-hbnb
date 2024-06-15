#!/usr/bin/env python3

from flask import Blueprint, request, jsonify, current_app
from app.models.user import User

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(k in data for k in ('email', 'first_name', 'last_name')):
        return jsonify({'error': 'Missing required fields'}), 400

    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']

    data_manager = current_app.config['DATA_MANAGER_USER']

    for user in data_manager.data:
        if user['_email'] == email:
            return jsonify({'error': 'Email already exists'}), 409

    user = User(email=email, first_name=first_name, last_name=last_name)
    data_manager.save(user.to_dict())

    return jsonify(user.to_dict()), 201


@user_bp.route('/users', methods=['GET'])
def get_users():
    data_manager = current_app.config['DATA_MANAGER_USER']
    return jsonify(data_manager.data), 200


@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    data_manager = current_app.config['DATA_MANAGER_USER']
    user = data_manager.get_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200


@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing required data'}), 400

    data_manager = current_app.config['DATA_MANAGER_USER']
    user = data_manager.get_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    email = data.get('email', user['_email'])
    first_name = data.get('first_name', user['_first_name'])
    last_name = data.get('last_name', user['_last_name'])

    if email != user['_email']:
        for u in data_manager.data:
            if u['_email'] == email:
                return jsonify({'error': 'Email already exists'}), 409

    user['_email'] = email
    user['_first_name'] = first_name
    user['_last_name'] = last_name
    user['updated_at'] = User(email, first_name, last_name).updated_at

    data_manager.update(user)
    return jsonify(user), 200


@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    data_manager = current_app.config['DATA_MANAGER_USER']
    user = data_manager.get_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    data_manager.delete(user_id)
    return '', 204
