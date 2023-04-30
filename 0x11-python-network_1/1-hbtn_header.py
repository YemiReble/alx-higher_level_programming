#!/usr/bin/python3
"""
This python script sends a request to
the URL and displays the value of the X-Request-Id 
variable found in the header of the response
"""


import urllib.request
import sys

"""
Program collect url as a command line argument
"""
url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader("X-Request-Id")
    print(x_request_id)