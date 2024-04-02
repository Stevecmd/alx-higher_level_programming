#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an integer using "{:d}".format().

    Args:
        value (int): The integer to be printed.

    Returns:
        bool: Returns True if the integer is printed successfully,
              Returns False if a TypeError or ValueError occurs
                     (indicating that the provided value is not a valid integer).
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
