#!/usr/bin/python3
'''function that returns the dictionary description with simple data structure
'''


def class_to_json(obj):
    '''Function class_to_jason
        returns: builds a dictonary
    '''
    return obj.__dict__

