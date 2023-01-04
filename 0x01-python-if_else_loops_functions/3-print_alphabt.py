#!/usr/bin/python3
for letter in range(ord('a'), ord('z')+1):
    letter = chr(letter)
    if letter not in "qe":
        print(letter, end="")
