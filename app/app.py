#!/usr/bin/env python3

from flask import Flask, send_from_directory
from flask_restx import Api
from flask_swagger_ui import get_swaggerui_blueprint
from persistence.data_manager import DataManager
from api.amenity_route import amenity_bp
from api.city_route import city_bp
from api.place_route import place_bp
from api.country_route import country_bp
from api.user_route import user_bp
from api.review_route import review_bp
import os

app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = ' /swagger.yaml'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "HBNB API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route('/swagger.yaml')
def serve_swagger():
    return send_from_directory(os.getcwd(), 'swagger.yaml')

"""initialize the data manager"""
data_manager_users = DataManager("data/data_users.json")
data_manager_reviews = DataManager("data/data_reviews.json")
data_manager_places = DataManager("data/data_place.json")
data_manager_countries = DataManager("data/data_countries.json")
data_manager_cities = DataManager("data/data_cities.json")
data_manager_amenities = DataManager("data/data_amenities.json")

"""initialize the blueprints"""
app.config['DATA_MANAGER_USERS'] = data_manager_users
app.config['DATA_MANAGER_REVIEWS'] = data_manager_reviews
app.config['DATA_MANAGER_PLACES'] = data_manager_places
app.config['DATA_MANAGER_COUNTRIES'] = data_manager_countries
app.config['DATA_MANAGER_CITIES'] = data_manager_cities
app.config['DATA_MANAGER_AMENITIES'] = data_manager_amenities

"""Register blueprints"""
app.register_blueprint(amenity_bp, url_prefix='/api')
app.register_blueprint(city_bp, url_prefix='/api')
app.register_blueprint(country_bp, url_prefix='/api')
app.register_blueprint(place_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
