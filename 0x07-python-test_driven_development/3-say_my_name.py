#!/usr/bin/python3
"""Say my name"""


def say_my_name(first_name, last_name=""):
    """
    function prints My name is <first name> <last name>
    Arguments:
    first_name: strings
    last_name: strings
    Return:
    prints My name is <first_name> <last_name>
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
