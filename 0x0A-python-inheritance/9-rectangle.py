#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

from typing import Union
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of rectangle using BaseGeometry."""

    def __init__(self, width: int, height: int):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width: int = width
        super().integer_validator("height", height)
        self.__height: int = height

    def area(self) -> int:
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """Return the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
