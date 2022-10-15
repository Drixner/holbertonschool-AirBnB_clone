#!/usr/bin/python3
"""
Module FileStorage
"""

import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """ class File Storage serialize and deserialize JSON objects """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Set in __object the obj with the key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize __objects to JSON file """
        dictionary = {}
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as fd:
            json.dump(dictionary, fd)

    def reload(self):
        """ Deserialize __objects from JSON file """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as fd:
                obj_dict = json.load(fd)
                for obj in obj_dict.values():
                    cls_d = obj['__class__']
                    del obj['__class__']
                    self.new(eval(cls_d)(**obj))

            return
