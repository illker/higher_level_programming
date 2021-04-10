#!/usr/bin/python3
"""Error code"""


import urllib.request
import urllib.error
from sys import argv


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(argv[1]) as f:
            print(f.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
