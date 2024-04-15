#!/usr/bin/python3
"""Defines a function that adds new attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (object): The object to add the attribute to.
        att (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
