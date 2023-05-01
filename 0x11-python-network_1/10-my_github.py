#!/usr/bin/python3
"""
This is a python script that takes my username and password
using Github Api to display my Id.
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    var = HTTPBasicAuth(username, password)

    url = "https://api.github.com/user"
    response = requests.get(url, auth=var)

    print(response.json().get("id"))
