#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x integers from a list.

    Args:
        my_list (list): The list from which to print elements.
        x (int): The maximum number of integers to print from my_list.

    Returns:
        int: The number of integers successfully printed.
    """
    # Initialize the count of printed integers
    printed_integers = 0
    
    # Iterate over the elements in the list
    for item in my_list:
        try:
            # Attempt to convert the current item to an integer
            value = int(item)
            # Print the integer using "{:d}".format()
            print("{:d}".format(value), end="")
            # Increment the count of printed integers
            printed_integers += 1
            # Break the loop if the required number of integers have been printed
            if printed_integers >= x:
                break
        except (ValueError, TypeError):
            # Continue to the next item if conversion to integer fails
            continue
    
    # Print a newline character after printing the integers
    print("")
    
    # Return the number of integers printed
    return printed_integers
