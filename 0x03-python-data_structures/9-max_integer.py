#!/usr/bin/python3

def max_integer(my_list=[]):
    """Determine the maximum integer in a given list."""
    if not my_list:
        return None

    maximum = my_list[0]
    for num in my_list:
        if num > maximum:
            maximum = num

    return maximum
