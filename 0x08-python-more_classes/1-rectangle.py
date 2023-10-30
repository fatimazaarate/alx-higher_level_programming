#!/usr/bin/python3
'''
this is a class Rectangle that defines a rectangle
'''


class Rectangle:
    '''a class Rectangle with height and width attributes'''
    def __init__(self, width=0, height=0):
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        self._Rectangle__width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        self._Rectangle__height = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__height = value
