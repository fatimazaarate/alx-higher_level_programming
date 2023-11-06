#!/usr/bin/python3
"""
Write a function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specified class.

    Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to check if 'obj' inherits from.

    Returns:
    bool: True if 'obj' is an instance of a subclass of 'a_class',
    but not the exact same class as 'a_class'. False otherwise.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
