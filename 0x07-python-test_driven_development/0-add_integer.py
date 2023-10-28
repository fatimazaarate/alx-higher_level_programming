#!/usr/bin/python3
'''
Module for add_integer method
it adds two integers a and b
returns the sum of a and b
'''


def add_integer(a, b=98):
    '''
    Function that Adds two integers a & b
    '''

    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
