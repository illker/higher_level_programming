#!/usr/bin/python3
"""Def class Square with size"""


class Square:
    """method init size"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """property"""
    @property
    def size(self):
        return self.__size

    """property"""

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """method area"""

    def area(self):
        return self.__size ** 2
