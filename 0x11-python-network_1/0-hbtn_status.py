#!/usr/bin/python3
"""Fetches status URL using urllib python"""


import urllib.request

if __name__ == "__main__":
    urlcat = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(urlcat) as response:
        res = response.read()

        print("Body response:")
        print("\t- type:", type(res))
        print("\t- content:", res)
        print("\t- utf8 content:", res.decode('utf-8'))
