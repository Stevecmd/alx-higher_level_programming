#!/usr/bin/python3
"""Defines a Rectangle class and a Square subclass."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
