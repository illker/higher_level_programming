#!/usr/bin/python3
"""Max integer - Unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class init size"""

    def testmax(self):
        """Max of list"""

        self.assertEqual(max_integer([-1, -50, -4, -5]), -1)
        self.assertEqual(max_integer([66, 2, 0, -1, 5]), 66)
        self.assertEqual(max_integer([6, 6, 6]), 6)
        self.assertEqual(max_integer([2, -2]), 2)
        self.assertEqual(max_integer([8]), 8)
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
