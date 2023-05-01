#!/usr/bin/python3
"""
This is a python script that uses urllib.error.HTTPError
to manage HTTP status exceptions
"""

import urllib
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode("utf-8")
            print(data)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
