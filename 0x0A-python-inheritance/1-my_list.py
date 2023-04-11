#!/usr/bin/python3
""" Writing a class MyList that inherit
    from list
"""



class MyList(list):
    '''Represent a MyList
    '''
    
    def print_sorted(self):
        '''
        Prints the list, but sorted
        '''

        print(sorted(self))
