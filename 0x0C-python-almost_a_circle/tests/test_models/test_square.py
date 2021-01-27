#!/usr/bin/python3
"""Square testing"""

from models.base import Base
from models.square import Square
import unittest
import json


class SquareTesting(unittest.TestCase):
    """Class Rectangle testing"""

    def test_2(self):
        """testing 2"""
        with self.assertRaises(TypeError):
            pizza = Square()

    def test_3(self):
        """testing"""
        burger = Square(6)
        self.assertEqual(burger.size, 6)
        self.assertEqual(burger.x, 0)
        self.assertEqual(burger.y, 0)

    def test_4(self):
        """testing"""
        with self.assertRaises(TypeError):
            pizza = Square("jolberton")
        with self.assertRaises(TypeError):
            bacon = Square(4, {10: 2}, 8)
        with self.assertRaises(ValueError):
            Square(-2)

    def test_5(self):
        """testing"""
        with self.assertRaises(ValueError):
            Square(5, -1, 3)
        with self.assertRaises(ValueError):
            Square(5, 1, -3)

    def test_6(self):
        """testing"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            burger = Square(1, -1)


if __name__ == '__main__':
    unittest.main()
