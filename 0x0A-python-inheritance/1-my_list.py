#!/usr/bin/python3
"""
Defines an inherited list
"""

class MyList(list):
    """
    A custom list class that extends the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
