#!/bin/bash
# This is a bash script that takes in a URL, sends a request to that URL, and displays the
curl -s -o /dev/null -w '%{size_download}\n' "$1"
# curl -s "$1" | wc -c
