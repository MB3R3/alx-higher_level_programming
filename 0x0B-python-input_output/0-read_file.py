#!/usr/bin/python3

"""
Task 0
This is a function that prints
the contents of a file
with utf-8 encoding
"""


def read_file(filename=""):
    """
    the file - 'filename is read by
    thw function read_file

    """

    with open(filename, "r", encoding="utf-8") as f:
        for i in f
        print(i, end='')
