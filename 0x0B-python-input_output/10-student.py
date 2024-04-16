#!/usr/bin/python3

"""Defines a class Student."""


class Student:
    """
    Defines a student by age, first_name and last_name.
    """
    def __init__(self, age, last_name, first_name):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            age (int): The age of the student
            last_name (str): The last name of the student.
            first_name (str): The first name of the student.

        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve. Default is None.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return {
                "age": self.age,
                "last_name": self.last_name,
                "first_name": self.first_name
            }
        else:
            return {
                attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)
            }
