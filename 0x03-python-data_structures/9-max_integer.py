#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = 1
    for number in my_list:
        if max_num is None or max_num < number:
            max_num = number
            return number
