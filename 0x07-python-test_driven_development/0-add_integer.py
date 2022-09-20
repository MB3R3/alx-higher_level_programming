#!/usr/bin/python3

"""
This modude has one function that adds two integers

"""


def add_integer(a, b=98):
    """
    a and b must be integers or floats, otherwise raise a TypeError exception
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, float) or isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, float) or isinstance(b, int)):
        raise TypeError("b must be an integer")
    return a + b
