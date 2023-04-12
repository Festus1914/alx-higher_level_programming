#!/usr/bin/python3
'''Defines a class Student.'''


class Student:
    '''Module class students
    '''

    def __init__(self, first_name, last_name, age):
        ''' Method to __init__
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Method to Json
        '''
        if (type(attrs) == list and 
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self,k)}
        return self.__dict__

    def reload_from_json(self, json):
        ''' Replace all attribute of the student. 
        Args:
            json (dict): The key/value pairs to replace attributes with.
            '''
            for k, v in jason.items():
                setattr(self, k, v)
