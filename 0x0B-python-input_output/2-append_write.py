#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """appends a string at the end"""

    with open(filename, "a", encoding="utf-8") as burger:
        return burger.write(text)
