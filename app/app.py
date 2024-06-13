#!/usr/bin/env python3

from flask import Flask
import os
import json
from routes.user_routes import user_blueprint, load_users_from_file

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix='/users')

load_users_from_file()

if __name__ == '__main__':
    app.run(debug=True)
