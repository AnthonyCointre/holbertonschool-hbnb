#!/usr/bin/env python3

from app.models.base_model import BaseModel


class Place(BaseModel):
    """
    Classe Place qui hérite de BaseModel.
    """

    def __init__(self, place_id="", place_name="", place_description="", place_address="", place_city="", place_country="", place_owner_id=""):
        """
        Initialise une nouvelle instance de Place.
        """

        super().__init__(place_id)
        self.id = place_id
        self.name = place_name
        self.description = place_description
        self.address = place_address
        self.city = place_city
        self.country = place_country
        self.owner_id = place_owner_id
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """
        Ajoute un avis à la liste des avis.
        """

        self.reviews.append(review)

    def add_amenity(self, amenity):
        """
        Ajoute une commodité à la liste des commodités.
        """

        self.amenities.append(amenity)

    def __repr__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères du lieu.
        """

        return f"Place {self.id} {self.name} {self.description} {self.address} {self.city} {self.country} {self.owner_id}"
