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
        """
        __init__ method initializes the instances attributes.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """

        self.__width__ = width
        self.integer_validator("width", width)
        self.__height__ = height
        self.integer_validator("height", height)
