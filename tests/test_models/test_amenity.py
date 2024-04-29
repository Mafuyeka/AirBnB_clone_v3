#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
import os


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of Amenity class."""
        amenity = Amenity()
        self.assertEqual(str(type(amenity)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Amenity class."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(type(amenity.name), str)

    def test_save_method(self):
        """Tests the save method of Amenity class."""
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method of Amenity class."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(type(amenity_dict), dict)
        self.assertTrue('id' in amenity_dict)
        self.assertTrue('created_at' in amenity_dict)
        self.assertTrue('updated_at' in amenity_dict)
        self.assertTrue('name' in amenity_dict)

    def test_str_method(self):
        """Tests the __str__ method of Amenity class."""
        amenity = Amenity()
        amenity_str = str(amenity)
        self.assertTrue('[Amenity]' in amenity_str)
        self.assertTrue('id' in amenity_str)
        self.assertTrue('created_at' in amenity_str)
        self.assertTrue('updated_at' in amenity_str)
        self.assertTrue('name' in amenity_str)


if __name__ == "__main__":
    unittest.main()

