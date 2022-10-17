#!/usr/bin/python3
"""
Unittest for place module
"""
import os
import unittest
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Place(unittest.TestCase):
    """ Test for
    Place Class """

    def setUp(self):
        """set up the
        test for testing Places"""
        FileStorage._FileStorage__file_path = "test.json"
        self.place = Place()
        self.place.city_id = "666"
        self.place.user_id = "666"
        self.place.name = "Purgatory"
        self.place.description = "Hell"
        self.place.number_rooms = 6
        self.place.number_bathrooms = 6
        self.place.max_guest = 6
        self.place.price_by_night = 666
        self.place.latitude = 666.0
        self.place.longitude = 666.0
        self.place.amenity_ids = ["remarkable"]
        self.place.save()

    def test_atrr_type_place(self):
        """test attribute type for Place"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def testpublic(self):
        self.assertEqual(str, type(Place().id))

    def test_inheritance(self):
        """test subclass of BaseModel"""
        self.assertIsInstance(self.place, Place)

    def test_attr_Place(self):
        """chekcing amenity attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)


if __name__ == "__main__":
    unittest.main()
