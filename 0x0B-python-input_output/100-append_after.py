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
        lines = file.readlines()
        for i, line in enumerate(lines):
            temp_lines.append(line)
            if search_string in line:
                # Check if it's the last line or if the next line is not
                # the new_string to avoid duplicate insertions
                if (i == len(lines) - 1 or
                        lines[i + 1].strip() != new_string.strip()):
                    temp_lines.append(new_string)
    with open(filename, "w") as file:
        # Join the lines and write at once to avoid an extra newline at the end
        file.write("".join(temp_lines))
