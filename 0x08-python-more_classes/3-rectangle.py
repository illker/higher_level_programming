#!/usr/bin/python3
"""Simple rectangle"""


class Rectangle:
    """class rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """area calc"""

    def area(self):
        return self.__height * self.__width

    """perimeter calc"""

    def perimeter(self):
        if self.__height == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            str_rect = (('#' * self.__width + '\n') * self.__height)
            return str_rect[:-1]
