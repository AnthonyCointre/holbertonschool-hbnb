#!/usr/bin/env python3

import unittest
import os
import json
from app.persistence.data_manager import DataManager
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.city import City
from app.models.country import Country
from app.models.amenity import Amenity


class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager(
            'app/persistence/data/test_data_manager.json')
        self.user = User(
            email="test@gmail.com",
            first_name="John",
            last_name="Doe",
            data_manager=self.data_manager
        )
        self.place = Place(
            name="Test Place",
            description="A nice place to stay",
            address="123 Test St",
            city_id="city_123",
            latitude=37.7749,
            longitude=-122.4194,
            host_id="host_456",
            num_rooms=3,
            num_bathrooms=2,
            price_per_night=100,
            max_guests=4,
            amenity_ids=1,
            data_manager=self.data_manager
        )
        self.review = Review(
            place_id="place_123",
            user_id="user_456",
            rating=5,
            comment="Great place!",
            data_manager=self.data_manager
        )
        self.city = City(
            name="New York",
            country_id="US",
            data_manager=self.data_manager
        )
        self.country = Country(
            name="United States",
            code="US"
        )
        self.amenity = Amenity(
            name="WiFi",
            data_manager=self.data_manager
        )

    def tearDown(self):
        if os.path.exists('app/persistence/data/test_data_manager.json'):
            os.remove('app/persistence/data/test_data_manager.json')

    def test_init(self):
        self.assertIsInstance(self.data_manager.storage, dict)

    def test_load_from_json(self):
        with open('app/persistence/data/test_data_manager.json', 'w') as file:
            json.dump({
                "User": {
                    self.user.id: self.user.to_dict()
                }
            }, file)
        self.data_manager.load_from_json()
        self.assertIn('User', self.data_manager.storage)
        self.assertIn(self.user.id, self.data_manager.storage['User'])

    def test_dict_to_entity(self):
        user_data = self.user.to_dict()
        entity = self.data_manager.dict_to_entity('User', user_data)
        self.assertIsInstance(entity, User)
        self.assertEqual(entity.email, self.user.email)

    def test_save_user(self):
        saved_user = self.data_manager.save(self.user)
        self.assertEqual(saved_user, self.user)
        self.assertIn('User', self.data_manager.storage)
        self.assertIn(self.user.id, self.data_manager.storage['User'])
        self.assertEqual(
            self.data_manager.storage['User'][self.user.id], self.user)

    def test_get_user(self):
        self.data_manager.save(self.user)
        retrieved_user = self.data_manager.get(self.user.id, 'User')
        self.assertEqual(retrieved_user, self.user)

    def test_update_user(self):
        self.data_manager.save(self.user)
        self.user.first_name = "Updated John"
        updated_user = self.data_manager.update(self.user)
        self.assertEqual(updated_user.first_name, "Updated John")
        self.assertEqual(
            self.data_manager.storage['User'][self.user.id].first_name, "Updated John")

    def test_delete_user(self):
        self.data_manager.save(self.user)
        result = self.data_manager.delete(self.user.id, 'User')
        self.assertTrue(result)
        self.assertNotIn(self.user.id, self.data_manager.storage['User'])

    def test_save_to_json(self):
        self.data_manager.save(self.user)
        self.data_manager.save_to_json()

        with open('app/persistence/data/test_data_manager.json', 'r') as file:
            data = json.load(file)

        self.assertIn('User', data)
        self.assertIn(self.user.id, data['User'])
        self.assertEqual(data['User'][self.user.id], self.user.to_dict())


if __name__ == '__main__':
    unittest.main()
