#!/usr/bin/env python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Classe Amenity qui hérite de BaseModel.
    """

    def __init__(self, amenity_id="", amenity_name=""):
        """
        Initialise une nouvelle instance de Amenity.
        """

        super().__init__(amenity_id)
        self.id = amenity_id
        self.name = amenity_name

    def __repr__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de l'agrément.
        """

        return f"amenity {self.id} {self.name}"
