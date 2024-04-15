#!/usr/bin/python3
"""This module defines a function for looking up object attributes."""


def lookup(obj):
    """
    Return a list of an object's available attributes.

    Args:
        obj: The object whose attributes are to be looked up.

    Returns:
        A list of strings representing the available attributes of the object.
    """
    return dir(obj)
