#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = {}
    for n in a_dictionary:
        newdic[n] = a_dictionary[n] * 2
    return newdic
