#!/usr/bin/python3

"""Define a MagicClass matching the bytecode provided."""

import math

class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize MagicClass.

        Args:
            radius (int or float): The radius of the MagicClass.
        Raises:
            TypeError: If radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Compute the area of the MagicClass.

        Returns:
            float: The area of the MagicClass.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Compute the circumference of the MagicClass.

        Returns:
            float: The circumference of the MagicClass.
        """
        return 2 * math.pi * self.__radius
