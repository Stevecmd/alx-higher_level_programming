#!/usr/bin/python3

def magic_calculation(a, b):
    """Performing ByteCode calculation"""

    from magic_calculation_102 import add, sub
    
    # If a is less than b
    if a < b:
        # Initialize c with the result of adding a and b
        c = add(a, b)
        # Iterate through range 4 to 6
        for i in range(4, 6):
            # Add i to c
            c = add(c, i)
        return c

    else:
        # If a is greater than or equal to b, return the result of subtracting b from a
        return sub(a, b)
