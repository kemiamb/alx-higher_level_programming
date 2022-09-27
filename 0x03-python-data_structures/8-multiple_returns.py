#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first = None
    for i in range(len(sentence)):
        i = 0
        first = sentence[i]
    return (len(sentence), first)
