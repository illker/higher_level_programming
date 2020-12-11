#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for n in dir(hidden_4):
        if n[0] != "_":
            print(n)
