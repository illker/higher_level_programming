#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    line = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end="")
            line += 1
        except:
            pass
    print()
    return line
