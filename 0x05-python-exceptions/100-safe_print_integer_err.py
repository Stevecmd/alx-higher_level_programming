#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Prints an integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if the integer was printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception:", e, file=sys.stderr)
        return False
