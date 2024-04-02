#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct (function): A pointer to the function to execute.
        *args: Any number of arguments to pass to the function.

    Returns:
        The result of the function if successful, None otherwise.
    """
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return result
