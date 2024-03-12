#!/usr/bin/python3

def print_last_digit(number):
    """Prints and Returns the value of the last digit"""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
