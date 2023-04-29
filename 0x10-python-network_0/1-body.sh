#!/bin/bash
# This is a Bash script that takes in a URL, sends a GET request to the URL
curl -s "$1" | (read -r status; [ "$status" == "HTTP/1.1 200 OK" ] && cat)
