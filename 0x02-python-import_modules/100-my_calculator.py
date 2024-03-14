#!/usr/bin/python3

if __name__ == "__main__":
    """Main script to handle basic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    # Checking if the correct number of arguments is provided
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Dictionary to map operators to corresponding functions
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    # Check if the provided operator is valid
    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Convert arguments to integers
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # Perform operation and print result
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
