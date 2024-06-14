#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields, Namespace
from datetime import datetime

app = Flask(__name__)

api = Api(app, version='1.0', title='Amenity API',
          description='Endpoints for Amenity CRUD operations')

amenity_ns = Namespace('amenities', description='Amenity operations')

amenities_db = [
    {'id': 1, 'name': 'Wifi', 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'id': 2, 'name': 'Parking', 'created_at': datetime.now(),
     'updated_at': datetime.now()}
]
next_id = 3

amenity_model = api.model('Amenity', {
    'id': fields.Integer(readonly=True, description='Identifiant unique de l\'aménité'),
    'name': fields.String(required=True, description='Nom de l\'aménité'),
    'created_at': fields.DateTime(description='Date de création de l\'aménité'),
    'updated_at': fields.DateTime(description='Date de mise à jour de l\'aménité')
})


def serialize_amenity(amenity):
    """
    Convertir les objets datetime en chaîne dans les données d'agrément.
    """

    return {
        'id': amenity['id'],
        'name': amenity['name'],
        'created_at': amenity['created_at'].isoformat(),
        'updated_at': amenity['updated_at'].isoformat()
    }


@amenity_ns.route('/')
class AmenityList(Resource):
    """
    Classe AmentyList qui hérite de Ressource.
    """

    @amenity_ns.marshal_list_with(amenity_model)
    def get(self):
        """
        Récupérer toutes les aménités.
        """

        return [serialize_amenity(amenity) for amenity in amenities_db]

    @amenity_ns.expect(amenity_model)
    @amenity_ns.response(201, 'Amenity successfully created')
    @amenity_ns.response(400, 'Validation Error')
    def post(self):
        """
        Créer une nouvelle aménité.
        """

        data = request.json
        if not data.get('name'):
            return {'message': 'Le nom de l\'aménité est requis'}, 400

        for amenity in amenities_db:
            if amenity['name'] == data['name']:
                return {'message': 'Une aménité avec ce nom existe déjà'}, 400

        global next_id
        new_amenity = {
            'id': next_id,
            'name': data['name'],
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        next_id += 1
        amenities_db.append(new_amenity)
        return serialize_amenity(new_amenity), 201


@amenity_ns.route('/<int:amenity_id>')
class AmenityDetail(Resource):
    """
    Classe AmentyDetail qui hérite de Ressource.
    """

    @amenity_ns.marshal_with(amenity_model)
    @amenity_ns.response(200, 'Amenity found')
    @amenity_ns.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """
        Récupérer les détails d'une aménité spécifique.
        """

        for amenity in amenities_db:
            if amenity['id'] == amenity_id:
                return serialize_amenity(amenity)
        return {'message': 'Aménité non trouvée'}, 404

    @amenity_ns.expect(amenity_model)
    @amenity_ns.response(200, 'Amenity successfully updated')
    @amenity_ns.response(400, 'Validation Error')
    @amenity_ns.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """
        Mettre à jour une aménité existante.
        """

        data = request.json
        for amenity in amenities_db:
            if amenity['id'] == amenity_id:
                if not data.get('name'):
                    return {'message': 'Le nom de l\'aménité est requis'}, 400

                for other_amenity in amenities_db:
                    if other_amenity['id'] != amenity_id and other_amenity['name'] == data['name']:
                        return {'message': 'Une aménité avec ce nom existe déjà'}, 400

                amenity['name'] = data['name']
                amenity['updated_at'] = datetime.now()
                return serialize_amenity(amenity)
        return {'message': 'Aménité non trouvée'}, 404

    @amenity_ns.response(204, 'Amenity successfully deleted')
    @amenity_ns.response(404, 'Amenity not found')
    def delete(self, amenity_id):
        """
        Supprimer une aménité spécifique.
        """

        global amenities_db
        amenities_db = [
            amenity for amenity in amenities_db if amenity['id'] != amenity_id]
        return '', 204


api.add_namespace(amenity_ns)
