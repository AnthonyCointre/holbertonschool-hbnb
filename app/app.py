#!/usr/bin/env python3

import os
from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes.user_routes import user_bp
from app.routes.review_routes import review_bp
from app.routes.place_routes import place_bp
from app.routes.country_routes import country_bp
from app.routes.city_routes import city_bp
from app.routes.amenity_routes import amenity_bp
from app.persistence.data_manager import DataManager

port = os.getenv('PORT')

app = Flask(__name__)

data_manager_user = DataManager("app/persistence/data/data_user.json")
data_manager_review = DataManager("app/persistence/data/data_review.json")
data_manager_place = DataManager("app/persistence/data/data_place.json")
data_manager_country = DataManager("app/persistence/data/data_country.json")
data_manager_city = DataManager("app/persistence/data/data_city.json")
data_manager_amenity = DataManager("app/persistence/data/data_amenity.json")

app.config['DATA_MANAGER_USER'] = data_manager_user
app.config['DATA_MANAGER_REVIEW'] = data_manager_review
app.config['DATA_MANAGER_PLACE'] = data_manager_place
app.config['DATA_MANAGER_COUNTRY'] = data_manager_country
app.config['DATA_MANAGER_CITY'] = data_manager_city
app.config['DATA_MANAGER_AMENITY'] = data_manager_amenity

SWAGGER_URL = '/api/docs'
API_URL = '/swagger.yaml'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Documentation"
    }
)

app.register_blueprint(amenity_bp)
app.register_blueprint(city_bp)
app.register_blueprint(country_bp)
app.register_blueprint(place_bp)
app.register_blueprint(review_bp)
app.register_blueprint(user_bp)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/')
def home():
    return 'HBnB Evolution: Part 1 (Model + API)'


@app.route('/swagger.yaml')
def serve_swagger():
    return send_from_directory(os.getcwd(), 'swagger.yaml')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
