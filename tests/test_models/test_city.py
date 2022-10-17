#!/usr/bin/python3
"""
Unittest for city module
"""
import os
import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_City(unittest.TestCase):
    """ Test for
    city Class """

    def setUp(self):
        """set up the
        test for testing cities"""
        FileStorage._FileStorage__file_path = "test.json"
        self.city = City()
        self.city.name = "Oslo"
        self.city.save()

    def test_attributes_City(self):
        """chekcing if City have attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('id' in self.city.__dict__)
        self.assertEqual(hasattr(self.city, "name"), True)

    def test_instance_City(self):
        """checking for valid type"""
        self.assertTrue(type(self.city.name) is str)
        self.assertTrue(type(self.city.id) is str)

    def test_docstring_City(self):
        """checking docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_any_attribute(self):
        """ check attributes existance"""
        self.assertEqual(hasattr(self.city, "state_id"), True)
        self.assertEqual(hasattr(self.city, "name"), True)

    def testpublic(self):
        self.assertEqual(str, type(City().id))

    def test_save_City(self):
        """test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)
if __name__ == "__main__":
    unittest.main()
