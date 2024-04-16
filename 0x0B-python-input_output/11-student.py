#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """
    Defines a student by first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve. Default is None.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
                }

    def reload_from_json(self, json_data):
        """
        Replaces attributes of Student instance with values from dictionary.

        Args:
            json_data (dict): Dictionary containing attribute names and values.

        Returns:
            None
        """
        for key, value in json_data.items():
            setattr(self, key, value)
