#!/usr/bin/python3
"""
Defines an inherited list
"""

class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """Initializing the object"""
        super().__init__()

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))
