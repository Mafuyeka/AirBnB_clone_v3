#!/usr/bin/python3
"""Test for FileStorage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Test the FileStorage class.'''

    @classmethod
    def setUpClass(cls):
        """Set up for test class."""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Tear down for test class."""
        del cls.user

    def tearDown(self):
        """Tear down for test methods."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Test Pep8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix Pep8")

    def test_all(self):
        """Test the all method."""
        storage = FileStorage()
        objs = storage.all()
        self.assertIsNotNone(objs)
        self.assertEqual(type(objs), dict)
        self.assertIs(objs, storage._FileStorage__objects)

    def test_new(self):
        """Test the new method."""
        storage = FileStorage()
        objs = storage.all()
        user = User()
        user.id = 123456
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(objs[key])

    def test_reload_filestorage(self):
        """Test reloading FileStorage."""
        self.storage.save()
        root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
