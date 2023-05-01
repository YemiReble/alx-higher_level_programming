#!/usr/bin/python3
"""
This is a python script that send an HTTP
Request to a Url and print out the receipt
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(url)))
        print("\t- content: {}".format(data.decode("utf-8")))
