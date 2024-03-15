#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns the length of a string and its first character,
    or (0, None) if the string is empty."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
