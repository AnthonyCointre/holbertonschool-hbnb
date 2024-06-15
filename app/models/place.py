#!/usr/bin/env python3

from app.models.base_model import BaseModel


class Place(BaseModel):
    """
    Modèle de données représentant un lieu.
    """

    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids):
        """
        Initialiser une instance de Place.
        """

        super().__init__()
        self._name = name
        self._description = description
        self._address = address
        self._city_id = city_id
        self._latitude = latitude
        self._longitude = longitude
        self._host_id = host_id
        self._number_of_rooms = number_of_rooms
        self._number_of_bathrooms = number_of_bathrooms
        self._price_per_night = price_per_night
        self._max_guests = max_guests
        self._amenity_ids = amenity_ids

    def to_dict(self):
        """
        Convertir l'instance de Place en un dictionnaire de données.
        """

        return {
            "place_id": self.id,
            "name": self._name,
            "description": self._description,
            "address": self._address,
            "city_id": self._city_id,
            "latitude": self._latitude,
            "longitude": self._longitude,
            "host_id": self._host_id,
            "number_of_rooms": self._number_of_rooms,
            "number_of_bathrooms": self._number_of_bathrooms,
            "price_per_night": self._price_per_night,
            "max_guests": self._max_guests,
            "amenity_ids": self._amenity_ids,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
