#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    for n in range(1, len(sys.argv)):
        add = add + int(sys.argv[n])
    print(add)
