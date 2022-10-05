#!/usr/bin/python3

"""
Task 2
a function that returns True if the
object is exactly an instance of
the specified class, otherwise False.
"""


def is_same_class(obj, a_class):

    """
    function def is_same_class(obj, a_class):
    checks if the object(obj) is an instance of the
    class (a_class)
    Using the type operator we can check
    """

    if type(obj) is a_class:
        return True
    else:
        return False
