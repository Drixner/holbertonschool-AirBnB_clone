#!/usr/bin/python3
"""
Module FileStorage
"""

import json
import os.path



class FileStorage:
    """ class File Storgae """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ public instance method all """
        return FileStorage.__objects
