#!/usr/bin/python3
"""Def class Square with size"""


class Square:
    """method init size"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size > 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """method area"""

    def area(self):
        return self.__size ** 2
