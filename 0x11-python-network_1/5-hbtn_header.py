#!/usr/bin/python3
"""Response header value"""


import requests
from sys import argv

if __name__ == '__main__':
    burger = requests.get(argv[1])
    print(burger.headers.get('X-Request-Id'))
