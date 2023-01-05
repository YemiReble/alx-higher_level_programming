#!/usr/bin/python3
number = range(0, 100)
for num in number:
    print('{:02d}'.format(num), end=', ')
if num == 99:
    print()
