#!/usr/bin/env python3

from flask import Flask, request, jsonify
from models.user import User

app = Flask(__name__)

app.register_blueprint(User, url_prefix='/api/users')


if __name__ == '__main__':
    app.run(debug=True)
