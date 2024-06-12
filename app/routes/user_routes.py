#!/usr/bin/env python3

from flask import Blueprint, request, jsonify, abort
from uuid import uuid4
from datetime import datetime
import re
import json

user_blueprint = Blueprint('user', __name__)

users = {}

def save_users_to_file():
    with open('users.json', 'w') as file:
        json.dump(users, file)

def load_users_from_file():
    global users
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

class User:
    def __init__(self, email, first_name, last_name):
        self.id = str(uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def update(self, email=None, first_name=None, last_name=None):
        if email:
            self.email = email
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        self.updated_at = datetime.now().isoformat()

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        abort(400, description="Invalid email format.")

def validate_user_data(data):
    if not data or 'email' not in data or 'first_name' not in data or 'last_name' not in data:
        abort(400, description="Missing required fields.")
    validate_email(data['email'])
    if not data['first_name'] or not isinstance(data['first_name'], str):
        abort(400, description="Invalid first name.")
    if not data['last_name'] or not isinstance(data['last_name'], str):
        abort(400, description="Invalid last name.")

def add_user(user):
    if user.email in [u['email'] for u in users.values()]:
        abort(409, description="Email already exists.")
    users[user.id] = user.to_dict()
    save_users_to_file()

def get_user(user_id):
    return users.get(user_id)

def update_user(user_id, data):
    user = users.get(user_id)
    if user:
        if 'email' in data and data['email'] != user['email']:
            if data['email'] in [u['email'] for u in users.values()]:
                abort(409, description="Email already exists.")
        user_obj = User(**user)
        user_obj.update(**data)
        users[user_id] = user_obj.to_dict()
        save_users_to_file()
        return user_obj.to_dict()
    else:
        abort(404, description="User not found.")

def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        save_users_to_file()
    else:
        abort(404, description="User not found.")

@user_blueprint.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    validate_user_data(data)
    user = User(data['email'], data['first_name'], data['last_name'])
    add_user(user)
    return jsonify(user.to_dict()), 201

@user_blueprint.route('', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@user_blueprint.route('/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user), 200
    else:
        abort(404, description="User not found.")

@user_blueprint.route('/<user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    data = request.get_json()
    validate_user_data(data)
    updated_user = update_user(user_id, data)
    return jsonify(updated_user), 200

@user_blueprint.route('/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    delete_user(user_id)
    return '', 204
