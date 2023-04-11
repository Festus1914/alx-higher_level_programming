#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""




class BaseGeometry:
    """Represent base geometry."""


    def area(self):
        """Not implimented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Creating a function integer_validator"""
        self.name = name
        self.value = value

        """
            Creating a conditional statements
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if type(value) <= 0:
            raise ValueError(name + "must be greater than 0")

class Rectangle(BaseGeometry):
    """Representing the rectangle by using Geometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle"""

        self.integer_validator("width, width")
        self.__width = width
        self.integer_validator("height, height")
        self.__height = height
