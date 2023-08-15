#!/usr/bin/python3
def multiple_returns(sentence):
    character = len(sentence)
    if character == 0:
        return 0, None
    return len(sentence), sentence[0]
