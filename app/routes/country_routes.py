#!/usr/bin/env python3

from flask import jsonify, request, Flask
from flask_restful import Resource, Api
from app.models.country import Country


class CountryList:
    def __init__(self, country_id, name):
        self.country_id = country_id
        self.name = name

    @classmethod
    def get(cls, country_code):
        # Placeholder for actual data retrieval logic
        if country_code == "US":
            return cls(country_id="US", name="United States")
        elif country_code == "CA":
            return cls(country_id="CA", name="Canada")
        return None

    @classmethod
    def get_all(cls):
        # Placeholder for actual data retrieval logic
        return [
            cls(country_id="US", name="United States"),
            cls(country_id="CA", name="Canada"),
        ]

class CountryResource(Resource):
    def get(self, country_code=None):
        if country_code:
            country = CountryList.get(country_code)
            if country:
                return {'country_id': country.country_id, 'name': country.name}, 200
            return {'error': 'Country not found'}, 404
        else:
            countries = CountryList.get_all()
            return [{'country_id': country.country_id, 'name': country.name} for country in countries], 200
