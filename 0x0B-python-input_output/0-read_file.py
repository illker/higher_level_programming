#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """ reads a text file"""

    with open(filename, "r", encoding="utf-8") as burger:
        print(burger.read())
