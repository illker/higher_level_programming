#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """writes a string to a text"""

    with open(filename, "w", encoding="utf-8") as burger:
        return burger.write(text)
