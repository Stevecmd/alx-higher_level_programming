#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """Main script to print all names defined by hidden_4 module."""

    # Getting all names defined in the hidden_4 module
    names = dir(hidden_4)

    # Printing names excluding those starting with "__"
    for name in names:
        if name[:2] != "__":
            print(name)
