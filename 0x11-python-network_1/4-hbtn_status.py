#!/usr/bin/python3
"""
This is a python script that send an HTTP
Request to a Url and print out the receipt
using the requests Model
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    data = requests.get(url)
    # data = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(data.content)))
    print("\t- content: {}".format(data.content))
