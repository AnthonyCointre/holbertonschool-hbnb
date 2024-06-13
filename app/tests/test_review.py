#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Classe de tests pour la classe Review.
    Utilise le framework de tests unitaires unittest.
    """

    def setUp(self):
        """
        Configure une instance de Review avant chaque test.
        """

        self.review = Review(review_id="review_1", user="user_1", place="place_1")

    def test_review_initialization(self):
        """
        Teste si l'instance de Review est correctement initialisée.
        """

        self.assertEqual(self.review.review_id, "review_1")
        self.assertEqual(self.review.user, "user_1")
        self.assertEqual(self.review.place, "place_1")

    def test_repr(self):
        """
        Teste la méthode __repr__ pour la représentation en chaîne de caractères de l'avis.
        """

        expected_repr = "Review(review_1, user_1, place_1)"
        self.assertEqual(repr(self.review), expected_repr)


if __name__ == '__main__':
    unittest.main()
