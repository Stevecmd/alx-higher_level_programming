#!/usr/bin/python3
"""Defines a Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance
        
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X coordinate of the rectangle's position.
            y (int): Y coordinate of the rectangle's position.
            id (int): Identifier of the rectangle. If None, a unique id is generated.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def check_y(self, value):
        """Check if y is non-negative"""
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height
