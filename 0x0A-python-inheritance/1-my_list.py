#!/usr/bin/python3
"""list of available attributes"""


class MyList(list):
    """sorted print"""

    def print_sorted(self):
        """prints"""
        print(sorted(self))
