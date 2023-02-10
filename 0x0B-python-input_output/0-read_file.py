#!/usr/bin/python3
""" A python programe that reads any file type"""


def read_file(filename=""):
    """Function that reads file"""
    with open(filename, 'r', encoding="UTF-8") as read_file:
        """Opening a file and reading it"""
        for line in read_file:
            """Looping through each line of the file"""
            print(line, end="")
