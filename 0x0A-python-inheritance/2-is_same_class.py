#!/usr/bin/python3
"""Check an instance of an Object"""


def is_same_class(obj, a_class):
    """ function that returns "True" if the object
        is exactly an instance of the specified
        class; otherwise False"""

    return (type(obj) == a_class)
