#!/usr/bin/python3

if __name__ == "__main__":
    """Main script to print the number of and list of arguments."""
    import sys

    # Counting the number of arguments
    count = len(sys.argv) - 1

    # Printing appropriate message based on the number of arguments
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Printing each argument along with its index
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
