#!/usr/bin/env python3

from models.base_model import BaseModel


class Country(BaseModel):
    """
    Classe Country qui hérite de BaseModel.
    """

    def __init__(self, country_id="", country_name=""):
        """
        Initialise une nouvelle instance de Country.
        """

        super().__init__(country_id)
        self.id = country_id
        self.name = country_name
        self.countries = []

    def add(self, country):
        """
        Ajoute un pays à la liste des pays.
        """

        self.countries.append(country)

    def __repr__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères du pays.
        """

        return f"country {self.id} {self.name}"
