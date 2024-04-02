#!/usr/bin/python3

def magic_calculation(a, b):
    """
    Perform a magic calculation based on the values of a and b.

    Args:
        a (int): The first parameter for the calculation.
        b (int): The second parameter for the calculation.

    Returns:
        int or float: The result of the magic calculation.
            If successful, returns the result of the calculation.
            If 'Too far' exception is raised, returns the sum of a and b.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError('Too far')
            result += a ** b / i
        except ValueError:
            result = b + a
            break
    return result
