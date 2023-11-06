#!/usr/bin/python3
"""
a class BaseGeometry
"""


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

        self.integer_validator("width", width)
        self.__width__ = width
        self.integer_validator("height", height)
        self.__height__ = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError(f"{self.value} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
