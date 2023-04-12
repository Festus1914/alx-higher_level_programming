#!/usr/bin/python3
'''Class Student that defines a student
'''


class student:
    '''Module class students
    '''

    def __init__(self, first_name, last_name, age):
        ''' Method to __init__
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Method to Json
        '''
        return self.__dict__
