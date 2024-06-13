#!/usr/bin/env python3

import unittest
import json
import sys
sys.path.append("..")
from routes.user_routes import user_bp
from flask import Flask

class UserRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(user_bp, url_prefix='/api')
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_create_user(self):
        data = {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post('/api/users', json=data)
        self.assertIn(response.status_code, [200, 201])

    def test_get_users(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)
        users = json.loads(response.data.decode('utf-8'))
        self.assertIsInstance(users, list)

    def test_get_specific_user(self):
        response = self.client.get('/api/users/1')
        self.assertIn(response.status_code, [200, 404])

    def test_update_user(self):
        data = {
            'email': 'updated_email@example.com',
            'first_name': 'Updated',
            'last_name': 'User'
        }
        response = self.client.put('/api/users/1', json=data)
        self.assertIn(response.status_code, [200, 404, 409])

    def test_delete_user(self):
        response = self.client.delete('/api/users/1')
        self.assertIn(response.status_code, [204, 404])

if __name__ == '__main__':
    unittest.main()
