#!/usr/bin/env python3

from app.models.base_model import BaseModel


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
    def to_dict(self):
        """
        Renvoie un dictionnaire contenant une représentation de la ville.
        """

        return {
            "id": self.id,
            "name": self.name,
            "country": self.country
        }

class CityCollection:
    """
    Classe CityCollection pour gérer une collection de villes.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance de CityCollection.
        """

        self.cities = []

    def add_city(self, city):
        """
        Ajoute une ville à la collection.
        """

        self.cities.append(city)
    
    def get_city(self, city_id):
        """
        Récupère une ville par son identifiant.
        """
        for city in self.cities:
            if city.id == city_id:
                return city
        return None

    def update_city(self, city_id, city_name):
        """ update city name """
        for city in self.cities:
            if city.id == city_id:
                city.name = city_name
                return city
    def delete_city(self, city_id):
        """ delete city """
        for city in self.cities:
            if city.id == city_id:
                self.cities.remove(city)
                return True
        return False
