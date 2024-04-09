#!/usr/bin/python3
"""
    Defines a locked class.
    with no class or object attribute
    that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name
"""


class LockedClass:
    """
    Prevent the user from instantiating new instance attributes
    except for 'first_name'.
    """

    __slots__ = ["first_name"]
