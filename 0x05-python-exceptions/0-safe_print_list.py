#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print up to x elements from a given list.

    Args:
        my_list (list): The list containing elements to print.
        x (int): The maximum number of elements to print.

    Returns:
        int: The actual number of elements printed.
    """
    printed_count = 0
    for item in my_list:
        try:
            if printed_count < x:
                print(item, end="")
                printed_count += 1
            else:
                break
        except IndexError:
            break
    print("")
    return printed_count
