#!/usr/bin/python3
'''Defines a file-writing function.'''


def write_file(filename="", text=""):
    '''Write a string to the UTF8 text file.

    Args:
        filename: This is the name of the file to write.
        text: This is the text to write to the file.
    Return:
    This is the number of characters written.
    '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
