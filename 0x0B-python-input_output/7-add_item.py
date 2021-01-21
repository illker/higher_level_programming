#!/usr/bin/python3
"""Load, add, save"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    file = load_from_json_file("add_item.json")
except:
    file = []
file.extend(sys.argv[1:])
save_to_json_file(file, "add_item.json")
