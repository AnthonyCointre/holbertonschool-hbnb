#!/usr/bin/env python3

import unittest
import sys
import os
from typing import List, Type, Any
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        """sets uo the test case environment"""
        self.data_manager = DataManager()
        
    def test_get(self):
        """ Test the method get"""
        self.assertIsNone(self.data_manager.get(Any, 1))
        
    def test_get_all(self):
        """Test the get all method"""
        self.assertIsNone(self.data_manager.get_all(Any), List)
    
    def test_save(self):
        """Test the save method"""
        self.assertIsNone(self.data_manager.save())
        
    def test_delete(self):
        """Test the delete method"""
        self.assertIsNone(self.data_manager.delete())
        
    def test_close(self):
        """Test the close method"""
        self.assertIsNone(self.data_manager.close())
        
if __name__ == '__main__':
    unittest.main()
