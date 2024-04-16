#!/usr/bin/python3
"""Function that writes Object to file in JSON"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and saved to the file.
        filename (str): The name - file to save the JSON representation to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
