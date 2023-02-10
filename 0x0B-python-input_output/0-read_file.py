#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding="UTF-8") as read_file:
        for line in read_file:
            print(line, end="")
