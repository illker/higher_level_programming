#!/usr/bin/python3
"""POST an email"""


from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    burger = {'email': argv[2]}
    burger = parse.urlencode(burger)
    burger = burger.encode('utf-8')
    with request.urlopen(url, burger) as f:
        print(f.read().decode('utf-8'))
