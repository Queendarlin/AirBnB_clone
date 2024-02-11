#!/usr/bin/python3
"""
Module containing the City class that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class representing a city object in the database
    """
    # inst = 0
    state_id = ""
    name = ""
