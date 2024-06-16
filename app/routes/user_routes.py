#!/usr/bin/env python3

from flask import Blueprint, jsonify, request, abort, current_app
from datetime import datetime
from app.models.user import User

user_bp = Blueprint('users', __name__)


@user_bp.route('/users', methods=['POST'])
def create_user():
    data_manager = current_app.config['DATA_MANAGER_USERS']
    data = request.json
    if not data or 'email' not in data:
        abort(400, 'Email cannot be empty.')
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    if not User.is_valid_email_format(email):
        abort(400, 'Invalid email format!')
    if not isinstance(email, str) or not isinstance(first_name, str) \
            or not isinstance(last_name, str):
        abort(400, 'Fields format is invalid.')
    if not email.strip() or not first_name.strip() or not last_name.strip():
        abort(400, 'Fields cannot be empty.')
    if data_manager.get_by_email(email):
        abort(409, 'Email already exists.')
    try:
        user = User(email, first_name, last_name, data_manager)
    except ValueError as e:
        abort(400, str(e))
    data_manager.save(user)
    return jsonify(user.to_dict()), 201


@user_bp.route('/users', methods=['GET'])
def get_users():
    data_manager = current_app.config['DATA_MANAGER_USERS']
    users = [user.to_dict()
             for user in data_manager.storage.get('User', {}).values()]
    return jsonify(users), 200


@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    data_manager = current_app.config['DATA_MANAGER_USERS']
    user = data_manager.get(user_id, 'User')
    if user is None:
        abort(404, 'User not found.')
    return jsonify(user.to_dict()), 200


@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data_manager = current_app.config['DATA_MANAGER_USERS']
    user = data_manager.get(user_id, 'User')
    if user is None:
        abort(404, 'User not found.')
    data = request.json
    if not data:
        abort(400, 'Data is invalid.')
    new_email = data.get('email', user.email)
    new_first_name = data.get('first_name', user.first_name)
    new_last_name = data.get('last_name', user.last_name)
    if 'email' in data and not isinstance(new_email, str):
        abort(400, 'Email format is invalid.')
    if 'first_name' in data and not isinstance(new_first_name, str):
        abort(400, 'First name format is invalid.')
    if 'last_name' in data and not isinstance(new_last_name, str):
        abort(400, 'Last name format is invalid.')
    if 'email' in data and not new_email.strip():
        abort(400, 'Email cannot be empty.')
    if 'first_name' in data and not new_first_name.strip():
        abort(400, 'First name cannot be empty.')
    if 'last_name' in data and not new_last_name.strip():
        abort(400, 'Last name cannot be empty.')
    try:
        user.email = new_email
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.updated_at = datetime.utcnow()
    except ValueError as e:
        abort(400, str(e))
    data_manager.update(user)
    return jsonify(user.to_dict()), 200


@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    data_manager = current_app.config['DATA_MANAGER_USERS']
    if not data_manager.delete(user_id, 'User'):
        abort(404, 'User not found.')
    return '', 204
