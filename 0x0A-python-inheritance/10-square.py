#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle
    Methods:
        __init__(self, size):
        area(self)
    """
    def __init__(self, size):
        """
        Initialization function.
        Attribute is private.
        Attribute:
            size(int): Size of the side of a square.
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Extends parent's empty method and returns area
        """
        return self.__size * self.__size
