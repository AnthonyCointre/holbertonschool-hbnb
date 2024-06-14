#!/usr/bin/env python3

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.models.city import City
from app.models.country import Country

from app.persistence.data_manager import DataManager


def main():
    # Initialize DataManager
    data_manager = DataManager()

    # Create entities
    user1 = User("user1@example.com", "password123", "John", "Doe")
    place1 = Place("Cozy House", "A beautiful house in the countryside",
                   "123 Green St", "Springfield", 42.35, -71.05, 3, 2, 100, 6)
    review1 = Review(user_id=user1.id, place_id=place1.id,
                     rating=4, comment="Great place to stay!")
    amenity1 = Amenity("Wi-Fi")
    city1 = City("Springfield")
    country1 = Country("USA")

    # Save entities
    data_manager.save(user1)
    data_manager.save(place1)
    data_manager.save(review1)
    data_manager.save(amenity1)
    data_manager.save(city1)
    data_manager.save(country1)

    # Retrieve entities
    retrieved_user = data_manager.get(user1.id, type(user1).__name__)
    retrieved_place = data_manager.get(place1.id, type(place1).__name__)
    retrieved_review = data_manager.get(review1.id, type(review1).__name__)
    retrieved_amenity = data_manager.get(amenity1.id, type(amenity1).__name__)
    retrieved_city = data_manager.get(city1.id, type(city1).__name__)
    retrieved_country = data_manager.get(country1.id, type(country1).__name__)

    print("Retrieved User:", retrieved_user)
    print("Retrieved Place:", retrieved_place)
    print("Retrieved Review:", retrieved_review)
    print("Retrieved Amenity:", retrieved_amenity)
    print("Retrieved City:", retrieved_city)
    print("Retrieved Country:", retrieved_country)

    # Update entity
    user1.last_name = "Smith"
    data_manager.update(user1)
    updated_user = data_manager.get(user1.id, type(user1).__name__)
    print("Updated User:", updated_user)

    # Delete entity
    data_manager.delete(place1.id, type(place1).__name__)
    deleted_place = data_manager.get(place1.id, type(place1).__name__)
    print("Deleted Place:", deleted_place)


if __name__ == "__main__":
    main()
