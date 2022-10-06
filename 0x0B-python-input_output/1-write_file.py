#!/usr/bin/python3

"""
Task 1
Write a function that writes a string
to a text file (UTF8) and returns the
number of characters written:
"""


def write_file(filename="", text=""):
    """
    Func write_file creates a file
    and writes text to it,
    or overrites an existing file with the same name.
    Finally returns the lenght of text
    """

    with open(filename, mode="w+", encoding="utf-8") as f:
        lenght = f.write(text)

    return lenght
