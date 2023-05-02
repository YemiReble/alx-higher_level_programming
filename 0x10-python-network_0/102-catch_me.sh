#!/bin/bash
#This is a python scrit that sends a request to a sever and make it return a message.
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
