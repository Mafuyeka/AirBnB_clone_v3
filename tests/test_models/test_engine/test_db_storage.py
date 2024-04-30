#!/usr/bin/python3
"""
Unit Test for DBStorage Class
"""
import unittest
from datetime import datetime
from models import *
import os
from models.base_model import Base
from models.engine.db_storage import DBStorage


storage_type = os.environ.get('HBNB_TYPE_STORAGE')


@unittest.skipIf(storage_type != 'db', 'skip if environ is not db')
class TestDBStorageDocs(unittest.TestCase):
    """Class for testing DBStorage docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('..... For DBStorage Class .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = ' Database engine '
        actual = db_storage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'handles long term storage of all class instances'
        actual = DBStorage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_all(self):
        """... documentation for all function"""
        expected = ' returns a dictionary of all objects '
        actual = DBStorage.all.__doc__
        self.assertEqual(expected, actual)

    def test_doc_new(self):
        """... documentation for new function"""
        expected = ' adds objects to current database session '
        actual = DBStorage.new.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """... documentation for save function"""
        expected = ' commits all changes of current database session '
        actual = DBStorage.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_reload(self):
        """... documentation for reload function"""
        expected = ' creates all tables in database & session from engine '
        actual = DBStorage.reload.__doc__
        self.assertEqual(expected, actual)

    def test_doc_delete(self):
        """... documentation for delete function"""
        expected = ' deletes obj from current database session if not None '
        actual = DBStorage.delete.__doc__
        self.assertEqual(expected, actual)


@unittest.skipIf(storage_type != 'db', 'skip if environ is not db')
class TestDBStorageFunctionality(unittest.TestCase):
    """Class for testing DBStorage Functionality"""

    def setUp(self):
        print('\n\n.................................')
        print('...... Testing DBStorage Functionality....')
        print('.................................\n\n')
        self.obj = State(name="California")
        self.obj.save()

    def tearDown(self):
        self.obj.delete()
        self.obj = None

    def test_all(self):
        """Tests the all method of DBStorage"""
        obj_dict = storage.all()
        self.assertIsNotNone(obj_dict)
        self.assertIn(str(self.obj.id), obj_dict.keys())

    def test_new(self):
        """Tests the new method of DBStorage"""
        new_obj = State(name="New York")
        storage.new(new_obj)
        storage.save()
        new_obj_dict = storage.all()
        self.assertIn(str(new_obj.id), new_obj_dict.keys())
        new_obj.delete()

    def test_get(self):
        """Tests the get method of DBStorage"""
        retrieved_obj = storage.get(State, self.obj.id)
        self.assertEqual(self.obj, retrieved_obj)

    def test_count(self):
        """Tests the count method of DBStorage"""
        obj_count = storage.count(State)
        self.assertGreaterEqual(obj_count, 1)

    def test_save(self):
        """Tests the save method of DBStorage"""
        self.obj.name = "Updated California"
        storage.save()
        retrieved_obj = storage.get(State, self.obj
