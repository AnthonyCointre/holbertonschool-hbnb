#!/usr/bin/env python3

from models.base_model import BaseModel


class City(BaseModel):
    """
    Classe City qui hérite de BaseModel.
    """

    def __init__(self, city_id="", city_name="", city_country=""):
        """
        Initialise une nouvelle instance de City.
        """

        super().__init__(city_id)
        self.id = city_id
        self.name = city_name
        self.country = city_country

    def __repr__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de la ville.
        """

        return f"city {self.id} {self.name} {self.country}"


class CityCollection:
    """
    Classe CityCollection pour gérer une collection de villes.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance de CityCollection.
        """

        self.cities = []

    def add(self, city):
        """
        Ajoute une ville à la collection.
        """

        self.cities.append(city)
