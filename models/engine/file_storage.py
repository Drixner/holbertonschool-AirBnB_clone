#!/usr/bin/python3
"""
Module FileStorage
"""

import json
import os.path


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
        from models.base_model import BaseModel
        from models.user import User

        dct = {'BaseModel': BaseModel,
               'User': User
               }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as fd:
                obj_dict = json.load(fd)
                for key, value in obj_dict.items():
                    self.new(dct[value['__class__']](**value))
            return
