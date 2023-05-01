#!/usr/bin/python3
"""
This is a python script that sends a request to the URL
and displays the body of the response If the HTTP status code
is greater than or equal to 400, print: Error code: followed
by the value of the HTTP status code
"""

import sys
import requests


if __name__ == "__main___":
    url = sys.argv[1]

    data = requests.get(url)

    if data.status_code >= 400:
        print("Error code: {}".format(data.status_code))
    else:
        print(data.text)
