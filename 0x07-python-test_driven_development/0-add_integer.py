#!/usr/bin/python3
"""Defines a function to add integers."""


def add_integer(a, b=98):
    """Return the integer addition of two numbers.

    This function takes two arguments, a and b,
    and returns their integer sum.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to
        be added. Default is 98.

    Raises:
        TypeError: If either a or b is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
