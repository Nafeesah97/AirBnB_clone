#!/usr/bin/python3
import uuid
from datetime import datetime

""""
This modeule contains a base class that contains all
attributes for other classes
Author: Nafeesah and Yebo
"""
class BaseModel():
    """
    A class which contains all attributes for others.

    Attributes:
        id(str): identification for each instances
        created_at(date): current datetime when an instance is created
        updated_at(date): current datetime when an instance is created and updated

    Methods:
        save(): updates the public instance attribute updated_at with the current datetime
        to_dict(): returns a dictionary containing all keys/values of __dict__

    Example:

    """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, id=None, created_at=None, updated_at = None):
        """To initialize class attributes"""
        self.id = BaseModel.id
        self.created_at = BaseModel.created_at
        self.updated_at = BaseModel.updated_at
    
    def __str__(self):
        """To overwrite"""
        return f"[{self.__class__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        return (self.updated_at)
    
    def to_dict(self):
        """ 
        returns a dictionary containing all keys/values of __dict__ of 
        the instance
        """
        dic = {}
        for key,val in self.__dict__.item():
            if key == 'created_at':
                val1 = val.strftime("%Y-%m-%dT%H:%M:%S.%f")
                dic[key] = val1
            elif key == 'updated_at':
                val2 = val.strftime("%Y-%m-%dT%H:%M:%S.%f")
                dic[key] = val2
            else:
                dic[key] = val
        dic[__class__] = self.__class__
        return (dic)