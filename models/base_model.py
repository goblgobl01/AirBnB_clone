#!/usr/bin/python3
"""
a script that represent the baseModel class.
"""
import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel class represents the basemodel for all other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        Parameters:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in {'created_at', 'updated_at'}:
                        value = datetime.datetime.fromisoformat(value)
                        setattr(self, key, value)
                    else:
                        setattr(self, key, value)
                else:
                    continue

    def __str__(self):
        """
        return a string representation of the class.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates 'updated_at' attribute, saves the instance to storage.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.
        """
        my_dict = {}
        my_dict.update(self.__dict__)
        my_dict['created_at'] = datetime.datetime.isoformat(self.created_at)
        my_dict['updated_at'] = datetime.datetime.isoformat(self.updated_at)
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
