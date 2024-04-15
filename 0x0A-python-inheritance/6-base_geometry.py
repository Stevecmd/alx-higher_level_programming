#!/usr/bin/python3
"""Defines the base geometry class BaseGeometry."""

class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """Compute the area of the geometry.

        Raises:
            Exception: Message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')