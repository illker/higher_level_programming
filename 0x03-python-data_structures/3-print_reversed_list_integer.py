#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    for n in range(len(my_list)):
        a = a - 1
        print("{}".format(my_list[a]))
