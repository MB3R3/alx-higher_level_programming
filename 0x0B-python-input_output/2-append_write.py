#!/usr/bin/python3

"""
Task 2
Write a function that appends 
a string at the end of a text file (UTF8) 
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    func append_write appends text to a file
    and creates the file if it does not exist
    and finally returns the lenght
    """
    with open(filename, mode="a+", encoding="utf-8") as f:
        lenght = f.write(text)

    return lenght
