#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = []
    if my_list:
        for n in my_list:
            if n % 2 == 0:
                a.append(True)
            else:
                a.append(False)
        return a
