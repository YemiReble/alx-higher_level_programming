#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        sen = sentence[0]

    else:
        sen = None
    return (len(sentence), sen)
