#!/usr/bin/python3
"""This actually defines the locked class """


class LockdClass:
    """
    prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name
    """

    __slots_ = ["first_name"]
