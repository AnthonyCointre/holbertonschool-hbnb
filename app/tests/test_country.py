#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel
from models.country import Country


class TestCountry(unittest.TestCase):
    """
    Classe de tests pour la classe Country.
    Utilise le framework de tests unitaires unittest.
    """

    def setUp(self):
        """
        Configure une instance de Country avant chaque test.
        """

        self.country = Country(country_id="1", country_name="France")

    def test_country_initialization(self):
        """
        Teste si l'instance de Country est correctement initialisée.
        """

        self.assertEqual(self.country.id, "1")
        self.assertEqual(self.country.name, "France")

    def test_add_country(self):
        """
        Teste la méthode add pour ajouter des pays à la liste.
        """

        new_country = Country(country_id="2", country_name="Germany")
        self.country.add(new_country)
        self.assertIn(new_country, self.country.countries)

    def test_repr(self):
        """
        Teste la méthode __repr__ pour la représentation en chaîne de caractères du pays.
        """

        expected_repr = "country 1 France"
        self.assertEqual(repr(self.country), expected_repr)


if __name__ == '__main__':
    unittest.main()
