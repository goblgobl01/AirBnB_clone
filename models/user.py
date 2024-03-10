#!/usr/bin/python3
"""
Module for user.py
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    attributes:
        the user's email, password, first name and last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
