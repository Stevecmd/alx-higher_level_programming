#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x integers from a list.

    Args:
        my_list (list): The list from which to print.
        x (int): Maximum number of integers to print.

    Returns:
        int: The number of integers printed.
    """
    # Initialize the count of printed integers
    printed_integers = 0
    
    # Iterate over the elements in range
    for item in range(0, x):
        try:
            # Attempt to convert the current item to an integer
            value = int(my_list[item])
            print("{:d}".format(value), end="")
            # Increment the count of printed integers
            printed_integers += 1
        except (ValueError, TypeError):
            # Continue to the next item
            continue
        except IndexError:
            # Break the loop if the index is out of range
            break
    
    # Print a newline character
    print("")
    
    # Return the number of integers printed
    return printed_integers
