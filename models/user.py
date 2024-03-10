#!/usr/bin/python3
"""
a script that defines the class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    class User
    attributes:
    the user's email, password, first name and last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
