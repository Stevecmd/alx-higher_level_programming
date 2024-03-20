#!/usr/bin/python3

def complex_delete(dictionary, target_value):
    """Delete keys with a specific value in a dictionary."""
    while target_value in dictionary.values():
        for key, value in dictionary.items():
            if value == target_value:
                del dictionary[key]
                break

    return dictionary
