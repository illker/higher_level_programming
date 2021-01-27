#!/usr/bin/python3
"""Base testing"""

from models.base import Base
from models.rectangle import Rectangle
import unittest
import json
import io
from contextlib import redirect_stdout


class RectangleTesting(unittest.TestCase):
    """Class Rectangle testing"""

    def test_2(self):
        """test type"""
        burger = Rectangle(10, 2, 0, 0, "hi")
        self.assertEqual(burger.id, "hi")
        bacon = Rectangle(10, 2, 0, 0, [12, 10])
        self.assertEqual(bacon.id, [12, 10])
        pizza = Rectangle(10, 2, 0, 0, {"key": 12, "value": 20})
        self.assertEqual(pizza.id, {'key': 12, 'value': 20})
        cheese = Rectangle(10, 2, 0, 0, (12, 10))
        self.assertEqual(cheese.id, (12, 10))

    def test_3(self):
        """test type"""
        with self.assertRaises(TypeError):
            burger = Rectangle()

    def test_4(self):
        """testing"""
        burger = Rectangle(24, 98, 2, 3)
        self.assertEqual(burger.width, 24)
        self.assertEqual(burger.height, 98)
        self.assertEqual(burger.x, 2)
        self.assertEqual(burger.y, 3)

    def test_5(self):
        """testing"""
        with self.assertRaises(TypeError):
            bacon = Rectangle("jolberton", 7)
        with self.assertRaises(TypeError):
            burg = Rectangle({"KEY": 10}, 4)

    def test_6(self):
        """testing"""
        burger = Rectangle(2, 5)
        self.assertEqual(burger.area(), 10)
        pizza = Rectangle(2, 4, 2, 1, 6)
        self.assertEqual(pizza.area(), 8)

    def test_7(self):
        """testing"""
        bacon = Rectangle(10, 2, 1, 9, 10)
        burger = bacon.to_dictionary()
        teamf = {'id': 10, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(burger, teamf)
        cheese = Rectangle(1, 1)
        cheese.update(**burger)
        self.assertEqual(str(cheese), "[Rectangle] (10) 1/9 - 10/2")
        self.assertNotEqual(bacon, cheese)


if __name__ == '__main__':
    unittest.main()
