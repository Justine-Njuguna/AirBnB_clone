#!/usr/bin/python3


import uuid
from datetime import datetime
from . import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    setattr(
                            self,
                            key,
                            datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                            )
        else:
            self.id = str(uuid.uuid4())  # Generate a unique ID
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """
        Updates the pub inst attr updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dict containing keys/values of __dict__ of the inst.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
