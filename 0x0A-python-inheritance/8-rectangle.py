#!/usr/bin/python3
"""
a class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Public instance method: def area(self):
    that raises an Exception with the message area()
    is not implemented
    """

    def __init__(self, width, height):
        '''
        width and height must be positive integers
        '''

        self.__width__ = width
        self.integer_validator("width", width)
        self.__height__ = height
        self.integer_validator("height", height)
