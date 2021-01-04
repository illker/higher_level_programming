#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        line = 0
        for n in range(0, x):
            print("{}".format(my_list[n]), end="")
            line += 1
        print()
        return line
    except:
        print()
        return line
