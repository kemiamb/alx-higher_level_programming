#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(len(sentence)):
        i = 0
        first = sentence[i]
        if len(sentence) == 0:
            first = None
    return (len(sentence), first)
