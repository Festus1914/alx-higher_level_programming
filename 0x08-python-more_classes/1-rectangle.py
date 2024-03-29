#!/usr/bin/python3
"""Creating a class that defines a Rectangle"""


class Rectangle:
    """Subtitute this with a Rectangle"""

    def __init__(self, width=0, height=0):
        """Creating a new Rectangle

        Args:
            width (int): The width of a new rectangle.
            height (int): The height of a new rectangle.
            """
        self. width = width
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

        """For height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height  = value
