#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if length == 0:
        return (None)
    
    first_letter = sentence[0]
    

    print("Length: {:d} - First character: {}".format(length, first_letter))
