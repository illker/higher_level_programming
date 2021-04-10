#!/usr/bin/python3
"""Response header value"""


import requests
from sys import argv

if __name__ == "__main__":

    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    d = r.json()
    print(d.get('id'))
