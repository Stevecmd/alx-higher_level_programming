#!/usr/bin/python3
"""Function that returns an object - JSON string"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string representing an object.

    Returns:
        object: Python data structure represented by JSON string.
    """
    return json.loads(my_str)
