#!/usr/bin/python3

"""Defines a class Student."""


class Student:
    """
    Defines a student by age, first_name and last_name.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            age (int): The age of the student
            last_name (str): The last name of the student.
            first_name (str): The first name of the student.

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
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
