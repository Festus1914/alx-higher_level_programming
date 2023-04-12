#!/usr/bin/python3
'''  function that writes an Object to a text file, using a JSON representation
'''
import json


def save_to_json_file(my_obj, filename):
    '''Function  save_to_json_file
    accepts python object and sends JSON representation files
    '''
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
