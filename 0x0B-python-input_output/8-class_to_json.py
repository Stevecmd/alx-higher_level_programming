#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: Dictionary representation - object serializabled.
    """
    return obj.__dict__
