#!/usr/bin/env python3

from flask import jsonify, request, Flask
from flask_restful import Resource, Api
from app.models.country import Country


class CountryList:
    """
    Classe CountryList.
    """

    def __init__(self, country_id, name):
        """
        Initialiser un objet CountryList avec l'identifiant et le nom du pays.
        """

        self.country_id = country_id
        self.name = name

    @classmethod
    def get(cls, country_code):
        """
        Endpoint pour récupérer les détails d'un pays en fonction du code pays.
        """

        if country_code == "US":
            return cls(country_id="US", name="United States")
        elif country_code == "CA":
            return cls(country_id="CA", name="Canada")
        return None

    @classmethod
    def get_all(cls):
        """
        Endpoint pour récupérer tous les pays disponibles.
        """

        return [
            cls(country_id="US", name="United States"),
            cls(country_id="CA", name="Canada"),
        ]


class CountryResource(Resource):
    """
    Classe CountryResource qui hérite de Resource.
    """

    def get(self, country_code=None):
        """
        Endpoint pour gérer les requêtes GET sur la ressource des pays.
        """

        if country_code:
            country = CountryList.get(country_code)
            if country:
                return {'country_id': country.country_id, 'name': country.name}, 200
            return {'error': 'Country not found'}, 404
        else:
            countries = CountryList.get_all()
            return [{'country_id': country.country_id, 'name': country.name} for country in countries], 200
