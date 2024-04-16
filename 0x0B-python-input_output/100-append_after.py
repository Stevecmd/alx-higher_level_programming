#!/usr/bin/python3
"""Defines a function for text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts line of text to file after line containing specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): String to insert after occurrence of search_string.

    Returns:
        None
    """
    temp_lines = []
    with open(filename, "r") as file:
        for line in file:
            temp_lines.append(line)
            if search_string in line:
                temp_lines.append(new_string + "\n")
    with open(filename, "w") as file:
        file.writelines(temp_lines)
