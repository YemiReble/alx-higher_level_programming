#!/usr/bin/python3
"""This modle returns the attributes and methods of an object"""


def lookup(obj):
    """Function that lookup the methon of an object"""

    list = dir(obj)
    return list
