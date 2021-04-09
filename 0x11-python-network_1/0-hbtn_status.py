#!/usr/bin/python3
"""Fetches an URL using 'urllib' python package"""


import urllib.request

urlcat = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(urlcat) as response:
    res = response.read()

    print("Body response:")
    print("\t- type:", type(res))
    print("\t- content:", res)
    print("\t- utf8 content:", res.decode('utf-8'))
