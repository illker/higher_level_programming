#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    n = sorted(a_dictionary.keys(), key=str.lower)
    for x in n:
        print("{:s}: {}".format(x, a_dictionary))
