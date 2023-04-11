#!/usr/bin/python3
"""Define a class function"""


def is_same_class(obj, a_class):
    """Creating a conditional of either True or False"""

    if type(obj) == a_class:
        """
        Returning the booleans
        """
        return True
    return False
