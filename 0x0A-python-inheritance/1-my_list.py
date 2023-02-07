#!/usr/bin/python3
"""This module returns a sorted list"""


class MyList(list):
    """ A Class Attribute that inherit from list and return
        the list as sorted"""
    def print_sorted(self):
        """ Print sorted list"""
        print(sorted(self))
