#!/usr/bin/python3

"""A module defining a Square class."""


class Square:
    """Represents a square geometric shape."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The length of the square's side.
                Defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be a non-negative integer")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
