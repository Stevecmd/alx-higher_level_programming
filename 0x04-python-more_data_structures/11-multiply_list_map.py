#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """Return a new list with all values multiplied by a number."""
    return list(map(lambda element: element * number, my_list))
