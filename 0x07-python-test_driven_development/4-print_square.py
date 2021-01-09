#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """
    function that prints a square with #
    Arguments:
    size: interger size of square
    Return:
    square with the character # by size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(size):
        for m in range(size):
            print("#", end="")
        print()
