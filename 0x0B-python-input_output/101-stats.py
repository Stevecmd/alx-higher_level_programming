#!/usr/bin/python3
"""Analyzes input data from standard input to generate metrics.

Upon processing every ten lines or upon receiving a
keyboard interruption (CTRL + C),
the script calculates and displays the following statistics:

The cumulative file size up to the current point.
The count of each encountered HTTP status code
up to the current point.
"""


def print_status_codes(size, status_codes):
    """Print accumulated metrics on status codes.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
