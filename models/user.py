#!/usr/bin/python3
"""
Module Containing User Class from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class representing a User object in the database
    """
    # inst = 0
    email = ""
    password = ""
    first_name = ""
    last_name = ""
