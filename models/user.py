#!/usr/bin/python3

"""
This module contains the class User
Author: Nafeesah and Yebo
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    A class that contains the detail of user.

    Attributes:
        email(str): empty string
        password(str): empty string
        first_name(str): empty string
        last_name(str): empty string

    Methods:
        None
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""