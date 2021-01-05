#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divlist = []
    for n in range(list_length):
        z = 0
        try:
            z = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            divlist.append(z)
    return divlist
