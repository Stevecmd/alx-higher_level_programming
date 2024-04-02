#!/usr/bin/python3

"""Define a MagicClass matching the bytecode provided."""

import math

class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize MagicClass.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
