#!/usr/bin/python3
for c in reversed(range(97, 123)):
    if c % 2 != 0:
        c = c - 32
    print("{}".format(chr(c)), end="")
