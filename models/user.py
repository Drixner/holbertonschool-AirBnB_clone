#!/usr/bin/python3
""" Module class User """

from models.base_model import BaseModel


class User(BaseModel):
    """ Class user that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
