#!/usr/bin/python3
"""
Unittest for state module
"""
import os
import unittest
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_State(unittest.TestCase):
    """ Test for
    State Class """

    def setUp(self):
        """set up the
        test for testing States"""
        FileStorage._FileStorage__file_path = "test.json"
        self.state = State()
        self.state.name = "Florida"
        self.state.save()

    def test_docstring_State(self):
        """checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_instance_State(self):
        """checking for valid type"""
        self.assertTrue(type(self.state.name) is str)

    def test_to_dict_State(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.state), True)

    def testpublic(self):
        self.assertEqual(str, type(State().id))

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)

if __name__ == "__main__":
    unittest.main()
