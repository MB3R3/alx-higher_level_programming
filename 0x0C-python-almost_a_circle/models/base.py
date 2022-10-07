#!/usr/bin/python3
"""
Write a class called Base.
"""


class Base:
    """
    class Base in which nb_objects is defined
    as Private class attribute.
    Methods:
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
        from_json_string(json_string):
        create(cls, **dictionary):
        load_from_file(cls):
    """
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
