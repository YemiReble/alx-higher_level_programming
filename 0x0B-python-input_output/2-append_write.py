#!/usr/bin/python3
""" A program that Append a New Line of Text to a file"""


def append_write(filename="", text=""):
    """Function that append a new text into a file"""
    with open(filename, 'a', encoding="UTF-8") as file_name:
        """Opening file and appeding the with the unicode encoding"""
        return file_name.write(text)
        """writing the new line to be appended to the file"""
