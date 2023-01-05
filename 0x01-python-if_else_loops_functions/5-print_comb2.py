#!/usr/bin/python3
number = range(0, 99)
for num in number:
    print('{:02d}'.format(num), end=', ')
if num == 98:
    print('99')
