#!/usr/bin/python3
"""
This is a python script that send a request
to a URL and return the out put to stdout
using <pipe> filename.py | cat -e
"""

import urllib.request

url = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(url) as response:
    res = response.read()
    print("Body Response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
    print("\t- utf8 content: {}".format(res.decode('utf-8')))
