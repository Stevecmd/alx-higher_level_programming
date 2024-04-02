#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists and returns a new list.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The maximum length to iterate

    Returns:
        list: A new list containing the division results.
    """
    result_list = []

    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            result = 0
            print("out of range")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        finally:
            result_list.append(result)

    return result_list
