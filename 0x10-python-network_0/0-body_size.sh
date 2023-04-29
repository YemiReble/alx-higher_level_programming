#!/usr/bin/env bash
# This is a bash script that takes in a URL, sends a request to that URL, and displays the
# size of the body of the response

curl -s -o /dev/null -w '%{size_download}\n' https://"$1"
