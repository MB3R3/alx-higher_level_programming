#!/usr/bin/python3
"""
class Base
with private class attribute
__nb_objects
"""
class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization function.
        If id is not None, assign the public instance
        attribute id with this argument value. Otherwise,
        increment __nb_objects and assign the new value
        to the public instance attribute id.
        Attributes:
            id: Number of identification.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
