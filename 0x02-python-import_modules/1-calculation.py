#!/usr/bin/python3

# If the script is executed directly
if __name__ == "__main__":
    # Importing the add, sub, mul, div functions from calculator_1 module
    from calculator_1 import add, sub, mul, div

    # Initializing variables
    a = 10
    b = 5

    # Performing addition and printing the result
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Performing subtraction and printing the result
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Performing multiplication and printing the result
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Performing division and printing the result
    print("{} / {} = {}".format(a, b, div(a, b)))
