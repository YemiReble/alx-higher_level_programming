#!/usr/bin/python3
"""
This is a python script that request from a url and
displays the value of the variable X-Request-Id
in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    data = requests.get(url)
    print(data.headers.get('X-Request-Id'))
