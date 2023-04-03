#!/usr/bin/python3
""" A program that returns an object (Python data structure) 
    represented by a JSON string
"""


import json


def from_json_string(my_str):
    """Function that returns the JSON Rep - Obj Str"""
    return json.dumps(my_str)
