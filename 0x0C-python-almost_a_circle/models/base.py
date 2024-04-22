#!/usr/bin/python3
import json
"""Defines a base model class."""


class Base:
    """
    Base class to manage id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of Base.

        Args:
            id (int): If provided, assigns the id to the instance.
                      If not provided, increments __nb_objects and
                      assigns the new value to id.
        """
        if id is not None:
            if id < 0:
                raise ValueError("id must be a non-negative integer")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
