#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Subtitute a rectangle"""
    def __init__(self, width = 0, height = 0):
        """Creating a new rectangle.

        Args:
        width (int): The width of a new rectangle.
        height (int): The height of a new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of a Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        ""'Return the perimeter of a Rectangle""'
        if self.__width == 0 or self.__height == 0:
            return(0)
        return((self.__width * 2) + (self.__height * 2)



