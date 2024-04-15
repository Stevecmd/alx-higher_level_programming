#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square."""

    def __init__(self, size):
        """Initializing a new square.

        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)
        self.__size = size
