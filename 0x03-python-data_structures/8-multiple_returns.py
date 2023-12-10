#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == '':
        firstCharacter = None
    else:
        firstCharacter = sentence[0]
    stringLength = len(sentence)
    returnTuple = (stringLength, firstCharacter)
    return returnTuple
