#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listkey = list(a_dictionary.keys())

    for value_dictionary in listkey:
        if value == a_dictionary.get(value_dictionary):
            del a_dictionary[value_dictionary]

    return (a_dictionary)
