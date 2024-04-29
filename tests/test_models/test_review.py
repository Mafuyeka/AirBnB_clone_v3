#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from models.review import Review
from models.base_model import BaseModel
from models import storage
import os


class TestReview(unittest.TestCase):
    """Test Cases for the Review class."""

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
        """Tests instantiation of Review class."""
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Review class."""
        review = Review()
        attributes = storage.attributes()["Review"]
        for attr, value in attributes.items():
            self.assertTrue(hasattr(review, attr))
            self.assertEqual(type(getattr(review, attr, None)), value)

    def test_save_method(self):
        """Tests the save method of Review class."""
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method of Review class."""
        review = Review()
        review.place_id = "Place123"
        review.user_id = "User123"
        review.text = "Great place to stay!"
        review_dict = review.to_dict()
        self.assertEqual(review_dict["id"], review.id)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["created_at"], review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"], review.updated_at.isoformat())
        self.assertEqual(review_dict["place_id"], "Place123")
        self.assertEqual(review_dict["user_id"], "User123")
        self.assertEqual(review_dict["text"], "Great place to stay!")

    def test_str_method(self):
        """Tests the __str__ method of Review class."""
        review = Review()
        review.place_id = "Place123"
        review.user_id = "User123"
        review.text = "Great place to stay!"
        review_str = str(review)
        self.assertTrue("[Review]" in review_str)
        self.assertTrue("place_id" in review_str)
        self.assertTrue("user_id" in review_str)
        self.assertTrue("text" in review_str)


if __name__ == "__main__":
    unittest.main()
