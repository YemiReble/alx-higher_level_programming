#!/usr/bin/python3
""" A programe that write into a file"""


def write_file(filename="", text=""):
    """Function that write into a file"""
    with open(filename, 'w', encoding="UTF-8") as file_name:
        """Openinig a file and writing into it"""
        return file_name.write(text)
        """Writing from text variable to filename"""
