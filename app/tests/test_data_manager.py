#!/usr/bin/env python3

import unittest
from datetime import datetime, timedelta
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.models.city import City
from app.models.country import Country
from app.persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):

    def setUp(self):
        # Initialize DataManager for testing
        self.data_manager = DataManager()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def test_save_and_get_user(self):
        # Create a User instance
        user = User("user1@example.com", "password123", "John", "Doe")

        # Save the User
        self.data_manager.save(user)

        # Retrieve the User by ID
        retrieved_user = self.data_manager.get(user.id, type(user).__name__)

        # Assert that retrieved_user matches the saved user
        self.assertEqual(retrieved_user.id, user.id)
        self.assertEqual(retrieved_user.email, user.email)
        self.assertEqual(retrieved_user.first_name, user.first_name)
        self.assertEqual(retrieved_user.last_name, user.last_name)

    def test_update_user(self):
        # Create and save a User instance
        user = User("user1@example.com", "password123", "John", "Doe")
        self.data_manager.save(user)

        # Update the User's last name
        user.last_name = "Smith"
        self.data_manager.update(user)

        # Retrieve the updated User
        updated_user = self.data_manager.get(user.id, type(user).__name__)

        # Assert that the last name has been updated
        self.assertEqual(updated_user.last_name, "Smith")

    def test_delete_user(self):
        # Create and save a User instance
        user = User("user1@example.com", "password123", "John", "Doe")
        self.data_manager.save(user)

        # Delete the User
        self.data_manager.delete(user.id, type(user).__name__)

        # Attempt to retrieve the deleted User
        deleted_user = self.data_manager.get(user.id, type(user).__name__)

        # Assert that deleted_user is None (not found)
        self.assertIsNone(deleted_user)

    def test_save_and_get_place(self):
        # Create a Place instance
        place = Place("Cozy House", "A beautiful house", "123 Green St", "Springfield", 42.35, -71.05, 3, 2, 100, 6)

        # Save the Place
        self.data_manager.save(place)

        # Retrieve the Place by ID
        retrieved_place = self.data_manager.get(place.id, type(place).__name__)

        # Assert that retrieved_place matches the saved place
        self.assertEqual(retrieved_place.id, place.id)
        self.assertEqual(retrieved_place.name, place.name)
        self.assertEqual(retrieved_place.description, place.description)
        self.assertEqual(retrieved_place.address, place.address)
        self.assertEqual(retrieved_place.city, place.city)
        self.assertEqual(retrieved_place.latitude, place.latitude)
        self.assertEqual(retrieved_place.longitude, place.longitude)
        self.assertEqual(retrieved_place.num_rooms, place.num_rooms)
        self.assertEqual(retrieved_place.num_bathrooms, place.num_bathrooms)
        self.assertEqual(retrieved_place.price_per_night, place.price_per_night)
        self.assertEqual(retrieved_place.max_guests, place.max_guests)

    def test_save_and_get_review(self):
        # Create a User and a Place to associate with the Review
        user = User("user1@example.com", "password123", "John", "Doe")
        self.data_manager.save(user)

        place = Place("Cozy House", "A beautiful house", "123 Green St", "Springfield", 42.35, -71.05, 3, 2, 100, 6)
        self.data_manager.save(place)

        # Create a Review instance
        review = Review(user.id, place.id, 4, "Great place to stay!")

        # Save the Review
        self.data_manager.save(review)

        # Retrieve the Review by ID
        retrieved_review = self.data_manager.get(review.id, type(review).__name__)

        # Assert that retrieved_review matches the saved review
        self.assertEqual(retrieved_review.id, review.id)
        self.assertEqual(retrieved_review.user, review.user)
        self.assertEqual(retrieved_review.place, review.place)
        self.assertEqual(retrieved_review.rating, review.rating)
        self.assertEqual(retrieved_review.comment, review.comment)

    def test_save_and_get_amenity(self):
        # Create an Amenity instance
        amenity = Amenity("Wi-Fi")

        # Save the Amenity
        self.data_manager.save(amenity)

        # Retrieve the Amenity by ID
        retrieved_amenity = self.data_manager.get(amenity.id, type(amenity).__name__)

        # Assert that retrieved_amenity matches the saved amenity
        self.assertEqual(retrieved_amenity.id, amenity.id)
        self.assertEqual(retrieved_amenity.name, amenity.name)

    def test_save_and_get_city(self):
        # Create a Country instance
        country = Country("USA")
        self.data_manager.save(country)

        # Create a City instance with a country
        city = City("Springfield", country.id)

        # Save the City
        self.data_manager.save(city)

        # Retrieve the City by ID
        retrieved_city = self.data_manager.get(city.id, type(city).__name__)

        # Assert that retrieved_city matches the saved city
        self.assertEqual(retrieved_city.id, city.id)
        self.assertEqual(retrieved_city.name, city.name)
        self.assertEqual(retrieved_city.country, city.country)

    def test_save_and_get_country(self):
        # Create a Country instance
        country = Country("USA")

        # Save the Country
        self.data_manager.save(country)

        # Retrieve the Country by ID
        retrieved_country = self.data_manager.get(country.id, type(country).__name__)

        # Assert that retrieved_country matches the saved country
        self.assertEqual(retrieved_country.id, country.id)
        self.assertEqual(retrieved_country.name, country.name)

if __name__ == "__main__":
    unittest.main()
