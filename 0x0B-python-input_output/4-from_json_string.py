#!/usr/bin/python3
'''Defines JSON to object functions.'''
import json


def from_json_string(my_str):
    '''Returns an object (Python data structure) represented by a JSON strin.g'''
    return json.loads(my_str)

