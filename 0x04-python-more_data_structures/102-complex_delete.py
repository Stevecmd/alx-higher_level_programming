#!/usr/bin/python3

def complex_delete(a_dictionary, target_value):
    """Delete keys with a specific value in a dictionary."""
    while target_value in a_dictionary.values():
        for key, value in a_dictionary.items():
            if value == target_value:
                del a_dictionary[key]
                break

    return a_dictionary
