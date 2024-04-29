#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage
import os


class TestPlace(unittest.TestCase):
    """Test Cases for the Place class."""

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
        """Tests instantiation of Place class."""
        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Place class."""
        place = Place()
        attributes = storage.attributes()["Place"]
        for attr, value in attributes.items():
            self.assertTrue(hasattr(place, attr))
            self.assertEqual(type(getattr(place, attr, None)), value)

    def test_save_method(self):
        """Tests the save method of Place class."""
        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method of Place class."""
        place = Place()
        place.name = "New Place"
        place.city_id = "City123"
        place.user_id = "User123"
        place.description = "A beautiful place"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 100
        place.latitude = 40.1234
        place.longitude = -74.5678
        place.amenity_ids = ["1", "2", "3"]
        place_dict = place.to_dict()
        self.assertEqual(place_dict["id"], place.id)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["created_at"], place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"], place.updated_at.isoformat())
        self.assertEqual(place_dict["name"], "New Place")
        self.assertEqual(place_dict["city_id"], "City123")
        self.assertEqual(place_dict["user_id"], "User123")
        self.assertEqual(place_dict["description"], "A beautiful place")
        self.assertEqual(place_dict["number_rooms"], 3)
        self.assertEqual(place_dict["number_bathrooms"], 2)
        self.assertEqual(place_dict["max_guest"], 6)
        self.assertEqual(place_dict["price_by_night"], 100)
        self.assertEqual(place_dict["latitude"], 40.1234)
        self.assertEqual(place_dict["longitude"], -74.5678)
        self.assertEqual(place_dict["amenity_ids"], ["1", "2", "3"])

    def test_str_method(self):
        """Tests the __str__ method of Place class."""
        place = Place()
        place.name = "New Place"
        place.city_id = "City123"
        place.user_id = "User123"
        place.description = "A beautiful place"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 100
        place.latitude = 40.1234
        place.longitude = -74.5678
        place.amenity_ids = ["1", "2", "3"]
        place_str = str(place)
        self.assertTrue("[Place]" in place_str)
        self.assertTrue("name" in place_str)
        self.assertTrue("city_id" in place_str)
        self.assertTrue("user_id" in place_str)
        self.assertTrue("description" in place_str)
        self.assertTrue("number_rooms" in place_str)
        self.assertTrue("number_bathrooms" in place_str)
        self.assertTrue("max_guest" in place_str)
        self.assertTrue("price_by_night" in place_str)
        self.assertTrue("latitude" in place_str)
        self.assertTrue("longitude" in place_str)
        self.assertTrue("amenity_ids" in place_str)


if __name__ == "__main__":
    unittest.main()
