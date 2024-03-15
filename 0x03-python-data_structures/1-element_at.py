#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves the element at the specified index from the given list"""
    if (idx < 0) or (idx > len(my_list) - 1):
        return None
    return(my_list[idx])
