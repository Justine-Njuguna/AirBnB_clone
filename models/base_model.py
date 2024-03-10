#!/usr/bin/python3


import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            kwargs (dict): Dict containing attribute names and their values.
        """
        if kwargs:
            # Recreate instance from dictionary representation
            for key, value in kwargs.items():
                if key == '__class__':
                    continue  # Skip '__class__' attribute
                elif key in ('created_at', 'updated_at'):
                    # Convert string to datetime object
                    setattr(
                            self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            # Create a new instance with unique ID and current timestamp
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public inst attr updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dict containing keys/values of __dict__ of the inst.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
