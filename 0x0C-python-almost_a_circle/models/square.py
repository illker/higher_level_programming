#!/usr/bin/python3
"""And now, the Square!"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init method"""

        super().__init__(size, size, x, y, id)
        self.size = size

    """setter and getter"""

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updates method"""
        pizza = ['id', 'size', 'x', 'y']
        if args and args[0] is not None:
            for bacon in range(len(args)):
                setattr(self, pizza[bacon], args[bacon])
        else:
            for burger in kwargs:
                setattr(self, burger, kwargs[burger])

    def to_dictionary(self):
        """Dict square"""
        return {'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y}
