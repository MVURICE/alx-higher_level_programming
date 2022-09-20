#!/usr/bin/python3
def remove_char_at(str, num):
    s = ""
    for i in range(len(str)):
        if i != num:
            s = s + str[i]
    return (s)
