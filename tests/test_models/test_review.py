#!/usr/bin/python3
"""
Unittest for review module
"""
import os
import unittest
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Review(unittest.TestCase):
    """ Test for
    Review Class """

    m = Review()

    def setUp(self):
        """set up the
        test for testing Reviews"""
        FileStorage._FileStorage__file_path = "test.json"
        self.rev = Review()
        self.rev.place_id = "666"
        self.rev.user_id = "666"
        self.rev.text = "666"
        self.rev.save()

    def test_atrr_type_review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.m.place_id), str)
        self.assertEqual(type(self.m.user_id), str)
        self.assertEqual(type(self.m.text), str)

    def test_attribute_place_id(self):
        """ Tests attr """
        self.assertEqual(hasattr(self.m, "place_id"), True)
        self.assertEqual(hasattr(self.m, "user_id"), True)
        self.assertEqual(hasattr(self.m, "text"), True)

    def test_subcls_Review(self):
        """test   subclass  BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)
        self.assertIsInstance(self.rev, Review)

    def test_docstring_Review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def testpublic(self):
        self.assertEqual(str, type(Review().id))


if __name__ == "__main__":
    unittest.main()
