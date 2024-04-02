#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists and returns a new list containing the results.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The maximum length to iterate through the lists.

    Returns:
        list: A new list containing the division results.
    """
    result_list = []

    for i in range(list_length):
        try:
            result = safe_print_division(my_list_1[i], my_list_2[i])
        except IndexError:
            result = 0
            print("out of range")
        finally:
            result_list.append(result)

    return result_list

def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float or None: The result of the division, or None if division by zero or invalid inputs occur.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = 0
        print("division by 0")
    except TypeError:
        result = 0
        print("wrong type")
    finally:
        return result
