#!/usr/bin/python3
"""Base testing"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json


class BaseTesting(unittest.TestCase):
    """Class Base testing"""

    def test_validate_str(self):
        """test strs in args"""
        burger = Base("cheese")
        pizza = Base(["cheese", "tomato"])
        lasagna = Base("bacon")
        self.assertEqual(burger.id, "cheese")
        self.assertEqual(pizza.id, ["cheese", "tomato"])
        self.assertEqual(lasagna.id, "bacon")

    def test_validate_none(self):
        """test without args"""
        burger = Base()
        self.assertEqual(burger.id, 1)
        pizza = Base()
        self.assertEqual(pizza.id, 2)

    def test_validate_int(self):
        """test int with args """
        burger = Base(6)
        self.assertEqual(burger.id, 6)
        pizza = Base(24)
        self.assertEqual(pizza.id, 24)

    def testing_json_string(self):
        """tests json string"""
        Base._Base__nb_objects = 0
        burger = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        pizza = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([burger, pizza])
        self.assertTrue(type(json_s) is str)
        fat = json.loads(json_s)
        self.assertEqual(fat, [burger, pizza])


if __name__ == "__main__":
    unittest.main()
