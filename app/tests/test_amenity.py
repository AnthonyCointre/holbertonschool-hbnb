#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Classe de tests pour la classe Amenity.
    Utilise le framework de tests unitaires unittest.
    """

    def setUp(self):
        """
        Configure une instance de Amenity avant chaque test.
        """

        self.amenity = Amenity(amenity_id="1", amenity_name="Pool")

    def test_amenity_initialization(self):
        """
        Teste si l'instance de Amenity est correctement initialisée.
        """

        self.assertEqual(self.amenity.id, "1")
        self.assertEqual(self.amenity.name, "Pool")

    def test_repr(self):
        """
        Teste la méthode __repr__ pour la représentation en chaîne de caractères de l'agrément.
        """

        expected_repr = "amenity 1 Pool"
        self.assertEqual(repr(self.amenity), expected_repr)


if __name__ == '__main__':
    unittest.main()
