#!/usr/bin/python3
""" Writing a class MyList that inherit
    from list
"""



class MyList(list):
    def print_sorted(self):
        print(sorted(self))
