#!/usr/bin/python3
# Author - Steve

def uppercase(str):
    """Convert and print a string of characters in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
