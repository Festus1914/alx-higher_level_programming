#!/usr/bin/python3
'''Defines the file-writing function.'''


def append_write(filename="", text=""):
    '''Writing a string to the UTF8 text file.

    Args:
        filename: This is the name of the file to write.
        text: This is the text to write to the file
    Returns:
        The number of characters written.
        '''
        with open(filename, "w", encoding="utf-8") as f:
            return f.write(text)



