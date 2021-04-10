#!/usr/bin/python3
"""Error code"""


import requests
from sys import argv

if __name__ == "__main__":
    burger = requests.get(argv[1])
    if burger.status_code >= 400:
        print("Error code:", burger.status_code)
    else:
        print(burger.text)
