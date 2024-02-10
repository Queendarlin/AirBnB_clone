#!/usr/bin/python3
"""
Module Containing Review Class from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class representing a Review object in the database
    """
    # inst = 0
    place_id = ""
    user_id = ""
    text = ""
