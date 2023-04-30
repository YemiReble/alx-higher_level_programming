#!/usr/bin/python3
"""
This is a script that takes in url and email
as input argument and sent a POST request to it
to displays the body of the response
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode()
    req = urllib.request.Request(url, data=data, method="POST")

    with urllib.request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print("Your email is: ".format(body))
