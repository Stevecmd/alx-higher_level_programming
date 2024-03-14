#!/usr/bin/python3

"""Importing the add function from add_0 module"""
from add_0 import add

"""Checking if the script is executed directly"""
if __name__ == "__main__":

    """Initializing variables"""
    a = 1
    b = 2

    """Printing the result of addition"""
    print("{} + {} = {}".format(a, b, add(a, b)))
