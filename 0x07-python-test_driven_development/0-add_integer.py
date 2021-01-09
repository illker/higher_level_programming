#!/usr/bin/python3
"""Integers addition"""


def add_integer(a, b=98):
    """
    Function calculates the add of 2 integers
    Arguments:
    a: integer var
    b: integer var
    Return:
    Result in integer
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
