#!/usr/bin/python3
"""
Module BaseModel
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """class BaseModel"""

    def __init__(self):
        """ constructor of BaseModel """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.strptime('%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = datetime.strptime('%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """ method string representation """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """  current datetime object """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ dictionary representation """

        dict_cp = self.__dict__.copy()
        dict_cp["created_at"] = self.created_at.isoformat()
        dict_cp["updated_at"] = self.updated_at.isoformat()
        dict_cp["__class__"] = self.__class__.__name__

        return dict_cp
