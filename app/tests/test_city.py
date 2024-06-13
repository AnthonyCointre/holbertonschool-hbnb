#!/usr/bin/env python3

import unittest
from app.models.base_model import BaseModel
from app.models.city import City, CityCollection


class TestCity(unittest.TestCase):
    """
    Classe de tests pour la classe City.
    Utilise le framework de tests unitaires unittest.
    """

    def setUp(self):
        """
        Configure une instance de City avant chaque test.
        """

        self.city = City(city_id="1", city_name="Paris", city_country="France")

    def test_city_initialization(self):
        """
        Teste si l'instance de City est correctement initialisée.
        """

        self.assertEqual(self.city.id, "1")
        self.assertEqual(self.city.name, "Paris")
        self.assertEqual(self.city.country, "France")

    def test_repr(self):
        """
        Teste la méthode __repr__ pour la représentation en chaîne de caractères de la ville.
        """

        expected_repr = "city 1 Paris France"
        self.assertEqual(repr(self.city), expected_repr)


class TestCityCollection(unittest.TestCase):
    """
    Classe de tests pour la classe CityCollection.
    Utilise le framework de tests unitaires unittest.
    """

    def setUp(self):
        """
        Configure une instance de CityCollection avant chaque test.
        """

        self.collection = CityCollection()

    def test_add_city(self):
        """
        Teste la méthode add pour ajouter des villes à la collection.
        """

        city = City(city_id="2", city_name="Lyon", city_country="France")
        self.collection.add(city)
        self.assertIn(city, self.collection.cities)


if __name__ == '__main__':
    unittest.main()
