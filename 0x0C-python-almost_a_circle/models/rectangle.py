#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method init"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """getter and setter width"""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """getter and setter height"""

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """getter and setter x"""

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """getter and setter y"""

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area calc"""
        return self.__height * self.__width

    def display(self):
        """Display #1"""
        for a in range(self.__y):
            print()
        for b in range(self.__height):
            print(" " * self.__x, end="")
            for b in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__"""
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        r = "Rectangle"
        return ("[{}] ({}) {}/{} - {}/{}".format(r, i, x, y, w, h))

    def update(self, *args, **kwargs):
        """method Update #1"""
        pizza = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            for bacon in range(len(args)):
                setattr(self, pizza[bacon], args[bacon])
        else:
            for burger in kwargs:
                setattr(self, burger, kwargs[burger])

    def to_dictionary(self):
        """Dict Rectangle"""
        burger = {}
        burger["id"] = self.id
        burger["width"] = self.width
        burger["height"] = self.height
        burger["x"] = self.x
        burger["y"] = self.y
        return burger
