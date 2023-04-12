#!/usr/bin/python3
'''Defines a  file appending function.'''


def append_write(filename="", text=""):
    '''Append a string to the end of the UTF8 text file.

    Args:
        filename: This is the name of the file to append.
        text: This is the string to append to the file.
    Returns:
        This is the number of characters appended.
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
