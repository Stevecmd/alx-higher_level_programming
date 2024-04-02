#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers from a list."""
    ret = 0
    
    for item in range(0, x):
        try:
            print("{:d}".format(my_list[item]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print("")
    return ret
