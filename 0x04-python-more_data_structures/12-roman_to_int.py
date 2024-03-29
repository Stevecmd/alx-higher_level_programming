#!/usr/bin/python3
def roman_to_int(roman_string):
    """ Convert roman string to digits
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    r_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    integer_value = 0

    for i in range(len(roman_string)):
        if r_numerals.get(roman_string[i], 0) == 0:
            return 0

        if (i != len(roman_string) - 1 and
                r_numerals[roman_string[i]] < r_numerals[roman_string[i + 1]]):
            integer_value -= r_numerals[roman_string[i]]
        else:
            integer_value += r_numerals[roman_string[i]]

    return integer_value
