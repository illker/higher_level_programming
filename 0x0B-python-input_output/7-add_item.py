#!/usr/bin/python3
"""Load, add, save"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json').load_from_json_file

try:
    n = load_from_json_file("add_item.json")
except:
    n = []

n = save_to_json_file(n + sys.argv[1:], "add_item.json")
