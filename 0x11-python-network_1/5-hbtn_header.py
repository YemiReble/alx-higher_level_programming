#!/usr/bin/python
"""
This is a python script that request from a url and
displays the value of the variable X-Request-Id
in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    headers = {X-Request-Id: '123'}
    data = requests.get(url, headers=headers)
    print(data.content)
