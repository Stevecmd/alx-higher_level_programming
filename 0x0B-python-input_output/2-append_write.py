#!/usr/bin/python3
"""Defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
