#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        sen = sentence[0]

    else:
        return None
    return (len(sentence), sen)
