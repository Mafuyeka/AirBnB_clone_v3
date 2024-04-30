import unittest
from models.engine.db_storage import DBStorage
from models.state import State
from models.user import User
from models.city import City
from models.base_model import BaseModel

class TestStorageGet(unittest.TestCase):
    """
    Testing `get()` method in DBStorage
    """

    @classmethod
    def setUpClass(cls):
        """
        setup tests for class
        """
        print('\n\n.................................')
        print('...... Testing Get() Method ......')
        print('.......... Place  Class ..........')
        print('.................................\n\n')

    def setUp(self):
        """
        setup method
        """
        self.storage = DBStorage()

    def test_get_method_obj(self):
        """
        testing get() method
        :return: True if pass, False if not pass
        """
        state = State(name="Florida")
        state.save()
        result = self.storage.get(cls="State", id=state.id)
        self.assertIsInstance(result, State)

    def test_get_method_return(self):
        """
        testing get() method for id match
        :return: True if pass, false if not pass
        """
        state = State(name="Florida")
        state.save()
        result = self.storage.get(cls="State", id=str(state.id))
        self.assertEqual(state.id, result.id)

    def test_get_method_none(self):
        """
        testing get() method for None return
        :return: True if pass, false if not pass
        """
        result = self.storage.get(cls="State", id="doesnotexist")
        self.assertIsNone(result)
