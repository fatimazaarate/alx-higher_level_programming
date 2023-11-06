#!/usr/bin/python3
"""
a class BaseGeometry
"""


class BaseGeometry:
    """
    Public instance method: def area(self):
    that raises an Exception with the message area()
    is not implemented
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError(f"{self.value} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
