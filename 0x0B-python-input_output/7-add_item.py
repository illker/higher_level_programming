#!/usr/bin/python3
""" Load, add, save """
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    n = load_from_json_file("add_item.json")
except:
    n = []
for a in range(1, len(sys.argv)):
    new_list.append(sys.argv[a])
save_to_json_file(new_list, "add_item.json")
