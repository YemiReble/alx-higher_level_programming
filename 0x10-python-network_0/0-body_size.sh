#!/bin/bash
# This is a bash script that takes in a URL, sends a request to that URL (curl -s "$1" | wc -c)
curl -s -o /dev/null -w '%{size_download}\n' "$1"
