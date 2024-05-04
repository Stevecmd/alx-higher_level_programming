#!/usr/bin/python3
"""Defines a function to add integers.

    Raises:
        TypeError: If either a or b is not an integer.
    """


def add_integer(a, b=98):
    """
    Adds two numbers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of the two numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
