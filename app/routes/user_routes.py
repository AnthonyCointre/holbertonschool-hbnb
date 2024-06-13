#!/usr/bin/env python3

from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields
import re

user_bp = Blueprint('user', __name__)
api = Api(user_bp, doc='/docs')

users = {}
user_id_counter = 1

user_model = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'email': fields.String(required=True, description='The email address of the user'),
    'first_name': fields.String(required=True, description='The first name of the user'),
    'last_name': fields.String(required=True, description='The last name of the user')
})

email_regex = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$')


def is_valid_email(email):
    return re.match(email_regex, email) is not None


@api.route('/users')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        return list(users.values()), 200

    @api.expect(user_model)
    def post(self):
        global user_id_counter
        data = request.json
        if not is_valid_email(data.get('email', '')):
            return {'message': 'Invalid email format'}, 400
        if any(user['email'] == data['email'] for user in users.values()):
            return {'message': 'Email already exists'}, 409
        if not data.get('first_name') or not data.get('last_name'):
            return {'message': 'First name and last name are required'}, 400

        user_id = user_id_counter
        user_id_counter += 1
        user = {
            'id': user_id,
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name']
        }
        users[user_id] = user
        return user, 201


@api.route('/users/<int:user_id>')
class User(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        user = users.get(user_id)
        if user is None:
            return {'message': 'User not found'}, 404
        return user

    @api.expect(user_model)
    def put(self, user_id):
        data = request.json
        user = users.get(user_id)
        if user is None:
            return {'message': 'User not found'}, 404
        if not is_valid_email(data.get('email', '')):
            return {'message': 'Invalid email format'}, 400
        if any(u['email'] == data['email'] and u['id'] != user_id for u in users.values()):
            return {'message': 'Email already exists'}, 409
        if not data.get('first_name') or not data.get('last_name'):
            return {'message': 'First name and last name are required'}, 400

        user.update({
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name']
        })
        return user

    def delete(self, user_id):
        if user_id not in users:
            return {'message': 'User not found'}, 404
        del users[user_id]
        return '', 204
