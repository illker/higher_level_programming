#!/usr/bin/python3
"""Def class Square with size"""


class Square:
    """square class methods"""

    def __init__(self, size=0, position=(0, 0)):
        """method init size"""

        self.size = size
        self.position = position

    """property"""

    @property
    def size(self):
        """size property"""

        return self.__size

    """property"""

    @size.setter
    def size(self, value):
        """size setter"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """property"""

    @property
    def position(self):
        """position property"""

        return self.__position

    """position setter"""

    @position.setter
    def position(self, value):
        """def position setter"""

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if all(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """method area"""

    def area(self):
        """method area"""

        return self.__size ** 2

    """print square"""

    def my_print(self):
        """size property"""

        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
