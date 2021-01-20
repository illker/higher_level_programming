#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """class MyInt"""

    def __eq__(self, value):
        """method eq"""
        return super().__ne__(value)

    def __ne__(self, value):
        """method ne"""
        return super().__eq__(value)
