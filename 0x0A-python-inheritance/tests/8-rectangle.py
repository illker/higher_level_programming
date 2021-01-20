#!/usr/bin/python3
"""Rectangle"""


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """method init"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
