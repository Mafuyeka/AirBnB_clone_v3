#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from models.state import State
from models.base_model import BaseModel
from models import storage
import os


class TestState(unittest.TestCase):
    """Test Cases for the State class."""

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
        """Tests instantiation of State class."""
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_attributes(self):
        """Tests the attributes of State class."""
        state = State()
        attributes = storage.attributes()["State"]
        for attr, value in attributes.items():
            self.assertTrue(hasattr(state, attr))
            self.assertEqual(type(getattr(state, attr, None)), value)

    def test_save_method(self):
        """Tests the save method of State class."""
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method of State class."""
        state = State()
        state.name = "California"
        state_dict = state.to_dict()
        self.assertEqual(state_dict["id"], state.id)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["created_at"], state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"], state.updated_at.isoformat())
        self.assertEqual(state_dict["name"], "California")

    def test_str_method(self):
        """Tests the __str__ method of State class."""
        state = State()
        state.name = "California"
        state_str = str(state)
        self.assertTrue("[State]" in state_str)
        self.assertTrue("name" in state_str)


if __name__ == "__main__":
    unittest.main()

