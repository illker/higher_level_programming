#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tca = tuple_a + (0, 0)
    tcb = tuple_b + (0, 0)
    return tca[0] + tcb[0], tca[1] + tcb[1]
