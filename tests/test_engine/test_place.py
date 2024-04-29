#!/usr/bin/python3
"""
Unit Test for Place Class
"""
import unittest
from datetime import datetime
from models.place import Place
import json
import os

storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class TestPlaceDocs(unittest.TestCase):
    """Class for testing Place docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.......  For the Place  ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nPlace Class from Models Module\n'
        actual = Place.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Place class handles all application places'
        actual = Place.__doc__
        self.assertEqual(expected, actual)


class TestPlaceInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  Place Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new place for testing"""
        self.place = Place()

    def test_instantiation(self):
        """... checks if Place is properly instantiated"""
        self.assertIsInstance(self.place, Place)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_to_string(self):
        """... checks if Place is properly casted to string"""
        my_str = str(self.place)
        my_list = ['Place', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_str = str(self.place)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.place.save()
        actual = type(self.place.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.place_json = self.place.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.place_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_json_class(self):
        """... to_json should include class key with value Place"""
        self.place_json = self.place.to_json()
        actual = None
        if self.place_json['__class__']:
            actual = self.place_json['__class__']
        expected = 'Place'
        self.assertEqual(expected, actual)

    def test_city_id_attribute(self):
        """... add city_id attribute"""
        self.place.city_id = "54321"
        if hasattr(self.place, 'city_id'):
            actual = self.place.city_id
        else:
            actual = ''
        expected = "54321"
        self.assertEqual(expected, actual)

    def test_user_id_attribute(self):
        """... add user_id attribute"""
        self.place.user_id = "12345"
        if hasattr(self.place, 'user_id'):
            actual = self.place.user_id
        else:
            actual = ''
        expected = "12345"
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """... add name attribute"""
        self.place.name = "Holberton"
        if hasattr(self.place, 'name'):
            actual = self.place.name
        else:
            actual = ''
        expected = "Holberton"
        self.assertEqual(expected, actual)

    def test_description_attribute(self):
        """... add description attribute"""
        self.place.description = "Awesome place"
        if hasattr(self.place, 'description'):
            actual = self.place.description
        else:
            actual = ''
        expected = "Awesome place"
        self.assertEqual(expected, actual)

    def test_number_rooms_attribute(self):
        """... add number_rooms attribute"""
        self.place.number_rooms = 5
        if hasattr(self.place, 'number_rooms'):
            actual = self.place.number_rooms
        else:
            actual = ''
        self.assertTrue(5 == actual)

    def test_number_bathrooms_attribute(self):
        """... add number_bathrooms attribute"""
        self.place.number_bathrooms = 2
        if hasattr(self.place, 'number_bathrooms'):
            actual = self.place.number_bathrooms
        else:
            actual = ''
        self.assertTrue(2 == actual)

    def test_max_guest_attribute(self):
        """... add max_guest attribute"""
        self.place.max_guest = 10
        if hasattr(self.place, 'max_guest'):
            actual = self.place.max_guest
        else:
            actual = ''
        self.assertTrue(10 == actual)

    def test_price_by_night_attribute(self):
        """... add price_by_night attribute"""
        self.place.price_by_night = 100
        if hasattr(self.place, 'price_by_night'):
            actual = self.place.price_by_night
        else:
            actual = ''
        self.assertTrue(100 == actual)

    def test_latitude_attribute(self):
        """... add latitude attribute"""
        self.place.latitude = 37.7749
        if hasattr(self.place, 'latitude'):
            actual = self.place.latitude
        else:
            actual = ''
        self.assertTrue(37.7749 == actual)

    def test_longitude_attribute(self):
        """... add longitude attribute"""
        self.place.longitude = 122.4194
        if hasattr(self.place, 'longitude'):
            actual = self.place.longitude
        else:
            actual = ''
        self.assertTrue(122.4194 == actual)

    def test_amenity_ids_attribute(self):
        """... add amenity_ids attribute"""
        self.place.amenity_ids = ["01", "02", "03"]
        if hasattr(self.place, 'amenity_ids'):
            actual = self.place.amenity_ids
        else:
            actual = ''
        expected = ["01", "02", "03"]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
