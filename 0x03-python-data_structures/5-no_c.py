#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [char for char in my_string if char.lower() != 'c']
    return "".join(copy)
