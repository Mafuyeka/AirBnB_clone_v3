#!/usr/bin/python3
"""Test for DBStorage"""
import unittest
import pep8
import json
import os
from os import getenv
import MySQLdb
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class."""

    @classmethod
    def setUpClass(cls):
        """Set up for test class."""
        cls.User = getenv("HBNB_MYSQL_USER")
        cls.Passwd = getenv("HBNB_MYSQL_PWD")
        cls.Db = getenv("HBNB_MYSQL_DB")
        cls.Host = getenv("HBNB_MYSQL_HOST")
        cls.db = MySQLdb.connect(host=cls.Host, user=cls.User,
                                 passwd=cls.Passwd, db=cls.Db,
                                 charset="utf8")
        cls.query = cls.db.cursor()
        cls.storage = DBStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """Tear down for test class."""
        cls.query.close()
        cls.db.close()

    def setUp(self):
        """Set up for test methods."""
        self.query.execute("TRUNCATE TABLE states")
        self.query.execute("TRUNCATE TABLE cities")
        self.query.execute("TRUNCATE TABLE users")
        self.query.execute("TRUNCATE TABLE places")
        self.query.execute("TRUNCATE TABLE reviews")
        self.query.execute("TRUNCATE TABLE amenities")
        self.query.execute("ALTER TABLE states AUTO_INCREMENT = 1")
        self.query.execute("ALTER TABLE cities AUTO_INCREMENT = 1")
        self.query.execute("ALTER TABLE users AUTO_INCREMENT = 1")
        self.query.execute("ALTER TABLE places AUTO_INCREMENT = 1")
        self.query.execute("ALTER TABLE reviews AUTO_INCREMENT = 1")
        self.query.execute("ALTER TABLE amenities AUTO_INCREMENT = 1")
        self.db.commit()

    def tearDown(self):
        """Tear down for test methods."""
        pass

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_pep8_DBStorage(self):
        """Test Pep8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix Pep8")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_read_tables(self):
        """Test if tables are read from the DB."""
        self.query.execute("SHOW TABLES")
        tables = self.query.fetchall()
        self.assertEqual(len(tables), 7)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_no_element_user(self):
        """Test if there are no elements in users table."""
        self.query.execute("SELECT * FROM users")
        users = self.query.fetchall()
        self.assertEqual(len(users), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_no_element_cities(self):
        """Test if there are no elements in cities table."""
        self.query.execute("SELECT * FROM cities")
        cities = self.query.fetchall()
        self.assertEqual(len(cities), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_add_state(self):
        """Test adding a new state."""
        self.query.execute("SELECT * FROM states")
        states_before = self.query.fetchall()
        self.assertEqual(len(states_before), 0)

        new_state = State(name="California")
        new_state.save()
        self.db.commit()

        self.query.execute("SELECT * FROM states")
        states_after = self.query.fetchall()
        self.assertEqual(len(states_after), 1)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_add_city(self):
        """Test adding a new city."""
        self.query.execute("SELECT * FROM cities")
        cities_before = self.query.fetchall()
        self.assertEqual(len(cities_before), 0)

        new_city = City(name="Los Angeles", state_id="CA")
        new_city.save()
        self.db.commit()

        self.query.execute("SELECT * FROM cities")
        cities_after = self.query.fetchall()
        self.assertEqual(len(cities_after), 1)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_add_user(self):
        """Test adding a new user."""
        self.query.execute("SELECT * FROM users")
        users_before = self.query.fetchall()
        self.assertEqual(len(users_before), 0)

        new_user = User(email="test@example.com", password="password")
        new_user.save()
        self.db.commit()

        self.query.execute("SELECT * FROM users")
        users_after = self.query.fetchall()
        self.assertEqual(len(users_after), 1)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_add_place(self):
        """Test adding a new place."""
        self.query.execute("SELECT * FROM places")
        places_before = self.query.fetchall()
        self.assertEqual(len(places_before), 0)

        new_place = Place(name="Cozy Cabin", city_id=1, user_id=1)
        new_place.save()
        self.db.commit()

        self.query.execute("SELECT * FROM places")
        places_after = self.query.fetchall()
        self.assertEqual(len(places_after), 1)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_add_review(self):
        """Test adding a new review."""
        self.query.execute("SELECT * FROM reviews")
        reviews_before = self.query.fetchall()
        self.assertEqual(len(reviews_before), 0)

        new_review = Review(text="Great place to stay!", place_id=1, user_id=1)
        new_review.save()
        self.db.commit()

        self.query.execute("SELECT * FROM reviews")
        reviews_after = self.query.fetchall()
        self.assertEqual(len(reviews_after), 1)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_add_amenity(self):
        """Test adding a new amenity."""
        self.query.execute("SELECT * FROM amenities")
        amenities_before = self.query.fetchall()
        self.assertEqual(len(amenities_before), 0)

        new_amenity = Amenity(name="WiFi")
        new_amenity.save()
        self.db.commit()

        self.query.execute("SELECT * FROM amenities")
        amenities_after = self.query.fetchall()
        self.assertEqual(len(amenities_after), 1)


if __name__ == "__main__":
    unittest.main()

