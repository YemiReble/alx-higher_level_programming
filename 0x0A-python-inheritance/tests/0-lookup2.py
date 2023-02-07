#!/usr/bin/python3
import inspect
"""Looking up the attributes and methods of an object"""


def lookup(obj):
    list = dir(obj)
    # list = inspect.getmembers(obj)
    return list
