#!/usr/bin/env python3

import unittest
import sys

sys.path.append("..")

from typing import List, Type, Any
from persistence.data_manager import DataManager


class TestDataManager(unittest.TestCase):
    """
    La classe de test TestDataManager teste les méthodes de la classe DataManager.
    """

    def setUp(self):
        """
        Méthode de configuration exécutée avant chaque test.
        """

        self.data_manager = DataManager()
        
    def test_get(self):
        """
        Teste la méthode get de DataManager.
        """

        self.assertIsNone(self.data_manager.get(Type[Any], 1))
        
    def test_get_all(self):
        """
        Teste la méthode get_all de DataManager.
        """

        self.assertIsNone(self.data_manager.get_all(Type[Any]), List)
    
    def test_save(self):
        """
        Teste la méthode save de DataManager.
        """

        self.assertIsNone(self.data_manager.save())
        
    def test_delete(self):
        """
        Teste la méthode delete de DataManager.
        """

        self.assertIsNone(self.data_manager.delete())
        
    def test_close(self):
        """
        Teste la méthode close de DataManager.
        """

        self.assertIsNone(self.data_manager.close())


if __name__ == '__main__':
    unittest.main()
