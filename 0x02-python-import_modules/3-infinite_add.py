#!/usr/bin/python3

if __name__ == "__main__":
    """Main script to print the addition of all arguments."""
    import sys

    # Initializing total sum
    total = 0

    # Iterating through each argument and adding to the total
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])

    # Printing the total sum
    print("{}".format(total))
