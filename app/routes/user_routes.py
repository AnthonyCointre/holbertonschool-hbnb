#!/usr/bin/env python3

from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields
import re

user_bp = Blueprint('user', __name__)

api = Api(user_bp, doc='/docs')

users = {}
user_id_counter = 1

user_model = api.model('User', {
    'id': fields.Integer(readOnly=True, description='Identifiant unique de l\'utilisateur'),
    'email': fields.String(required=True, description='Adresse email de l\'utilisateur'),
    'first_name': fields.String(required=True, description='Prénom de l\'utilisateur'),
    'last_name': fields.String(required=True, description='Nom de famille de l\'utilisateur')
})

email_regex = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$')


def is_valid_email(email):
    """
    Valider le format d'une adresse email en utilisant une expression régulière.
    """

    return re.match(email_regex, email) is not None


@api.route('/users')
class UserList(Resource):
    """
    Classe UserList qui hérite de Ressource.
    """

    @api.marshal_list_with(user_model)
    def get(self):
        """
        Endpoint pour obtenir la liste de tous les utilisateurs.
        """

        return list(users.values()), 200

    @api.expect(user_model)
    def post(self):
        """
        Endpoint pour créer un nouvel utilisateur.
        """

        global user_id_counter
        data = request.json

        if not is_valid_email(data.get('email', '')):
            return {'message': 'Format d\'email invalide'}, 400

        if any(user['email'] == data['email'] for user in users.values()):
            return {'message': 'Email déjà utilisé'}, 409

        if not data.get('first_name') or not data.get('last_name'):
            return {'message': 'Prénom et nom de famille sont obligatoires'}, 400

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
    """
    Classe User qui hérite de Ressource.
    """

    @api.marshal_with(user_model)
    def get(self, user_id):
        """
        Endpoint pour obtenir les détails d'un utilisateur spécifique par ID utilisateur.
        """

        user = users.get(user_id)
        if user is None:
            return {'message': 'Utilisateur non trouvé'}, 404
        return user

    @api.expect(user_model)
    def put(self, user_id):
        """
        Endpoint pour mettre à jour les détails d'un utilisateur spécifique par ID utilisateur.
        """

        data = request.json
        user = users.get(user_id)

        if user is None:
            return {'message': 'Utilisateur non trouvé'}, 404

        if not is_valid_email(data.get('email', '')):
            return {'message': 'Format d\'email invalide'}, 400

        if any(u['email'] == data['email'] and u['id'] != user_id for u in users.values()):
            return {'message': 'Email déjà utilisé'}, 409

        if not data.get('first_name') or not data.get('last_name'):
            return {'message': 'Prénom et nom de famille sont obligatoires'}, 400

        user.update({
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name']
        })
        return user

    def delete(self, user_id):
        """
        Endpoint pour supprimer un utilisateur spécifique par ID utilisateur.
        """

        if user_id not in users:
            return {'message': 'Utilisateur non trouvé'}, 404

        del users[user_id]
        return '', 204
