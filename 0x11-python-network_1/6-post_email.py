#!/usr/bin/python3
"""
This is a python script that sends a POST
request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    inst = {"email": sys.agrv[2]}
    resp = requests.post(url, data=inst)

    print(resp.text)
