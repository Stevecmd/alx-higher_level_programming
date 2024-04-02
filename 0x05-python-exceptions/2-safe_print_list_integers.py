#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers from a list."""
    printed_integers = 0
    
    for item in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_integers += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    
    print("")
    return printed_integers
