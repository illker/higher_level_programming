#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text"""

    with open(filename, "w", encoding="utf-8") as burger:
        return burger.write(json.dumps(my_obj))
