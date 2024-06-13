#!/usr/bin/env python3

from app.models.base_model import BaseModel


class User(BaseModel):
    """
    Classe User qui hérite de BaseModel.
    """

    def __init__(self, id, user_first_name="", user_last_name="", user_email=""):
        """
        Initialise une nouvelle instance de User.
        """

        super().__init__(id)
        self.email = user_email
        self.first_name = user_first_name
        self.last_name = user_last_name
        self.places = []

    def add_place(self, place_id):
        """
        Ajoute un lieu à la liste des lieux associés à l'utilisateur.
        """

        if place_id not in self.places:
            self.places.append(place_id)

    def __repr__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de l'utilisateur.
        """

        return f"User {self.id} {self.email} {self.first_name} {self.last_name}"
