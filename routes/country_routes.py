#!/usr/bin/env python3

from flask import jsonify, request, Flask
from flask_restful import Resource, Api
from models.country import Country


class CountryList(Resource):
    def __init__(self):
        """pre-load some countries"""
        self.countries = [
            Country(country_id="US", name="United States").save(),
            Country(country_id="FR", name="France").save()
        ]

    def get(self):
        """get all countries"""
        return jsonify([country.to_dict() for country in self.countries])

    def get(self.country_code):
        """get a country by country code"""
        country = Country.get(country_code)
        if country is not None:
            return jsonify(country.to_dict())
        else:
            return jsonify({"error": "Country not found"}), 404
