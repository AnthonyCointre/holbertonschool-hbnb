#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Classe de tests pour la classe User.
    Utilise le framework de tests unitaires unittest.
    """

    def setUp(self):
        """
        Configure une instance de User avant chaque test.
        """

        self.user = User(id=1, user_first_name="John", user_last_name="Doe", user_email="john.doe@example.com")

    def test_user_initialization(self):
        """
        Teste si l'instance de User est correctement initialisée.
        """

        self.assertEqual(self.user.id, 1)
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertEqual(self.user.places, [])

    def test_add_place(self):
        """
        Teste la méthode add_place pour ajouter des lieux à l'utilisateur.
        """

        self.user.add_place("place_1")
        self.assertIn("place_1", self.user.places)
        self.user.add_place("place_2")
        self.assertIn("place_2", self.user.places)
        self.user.add_place("place_1")
        self.assertEqual(self.user.places.count("place_1"), 1)

    def test_repr(self):
        """
        Teste la méthode __repr__ pour la représentation en chaîne de caractères de l'utilisateur.
        """

        expected_repr = "User 1 john.doe@example.com John Doe"
        self.assertEqual(repr(self.user), expected_repr)


if __name__ == '__main__':
    unittest.main()
