#!/usr/bin/python3

def multiple_returns(sentence):
    stringLength = len(sentence)
    firstCharacter = sentence[0]
    if sentence == '':
        firstCharacter = None
    returnTuple = (stringLength, firstCharacter)
    return returnTuple
