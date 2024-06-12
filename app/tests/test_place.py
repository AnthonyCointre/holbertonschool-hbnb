#!/usr/bin/env python3

import unittest
import sys

sys.path.append("..")

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Classe de tests pour la classe Place.
    Utilise le framework de tests unitaires unittest.
    """

    def setUp(self):
        """
        Configure une instance de Place avant chaque test.
        """

        self.place = Place(place_id="1", place_name="Eiffel Tower", place_description="Famous landmark in Paris",
                           place_address="Champ de Mars, 5 Avenue Anatole France", place_city="Paris", place_country="France", place_owner_id="owner_1")

    def test_place_initialization(self):
        """
        Teste si l'instance de Place est correctement initialisée.
        """

        self.assertEqual(self.place.id, "1")
        self.assertEqual(self.place.name, "Eiffel Tower")
        self.assertEqual(self.place.description, "Famous landmark in Paris")
        self.assertEqual(self.place.address, "Champ de Mars, 5 Avenue Anatole France")
        self.assertEqual(self.place.city, "Paris")
        self.assertEqual(self.place.country, "France")
        self.assertEqual(self.place.owner_id, "owner_1")
        self.assertEqual(self.place.reviews, [])
        self.assertEqual(self.place.amenities, [])

    def test_add_review(self):
        """
        Teste la méthode add_review pour ajouter des avis au lieu.
        """

        self.place.add_review("Amazing place!")
        self.assertIn("Amazing place!", self.place.reviews)
        self.place.add_review("Must visit!")
        self.assertIn("Must visit!", self.place.reviews)

    def test_add_amenity(self):
        """
        Teste la méthode add_amenity pour ajouter des commodités au lieu.
        """

        self.place.add_amenity("WiFi")
        self.assertIn("WiFi", self.place.amenities)
        self.place.add_amenity("Parking")
        self.assertIn("Parking", self.place.amenities)

    def test_repr(self):
        """
        Teste la méthode __repr__ pour la représentation en chaîne de caractères du lieu.
        """

        expected_repr = ("Place 1 Eiffel Tower Famous landmark in Paris "
                         "Champ de Mars, 5 Avenue Anatole France Paris France owner_1")
        self.assertEqual(repr(self.place), expected_repr)


if __name__ == '__main__':
    unittest.main()
