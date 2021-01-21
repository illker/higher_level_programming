#!/usr/bin/python3
"""object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""

    with open(filename, "r") as burger:
        return json.load(burger)
