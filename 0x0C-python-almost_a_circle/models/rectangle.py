#!/usr/bin/python3
"""
Define Rectangle module
"""
from models.base import Base

class Rectangle(Base):
    """
    creates a class that represents a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    @property
    def width(self):
        return self.__width
        
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.__width = value

    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value
        
    @property
    def x(self):
        return self.__x
        
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y
        
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        return self.width * self.height

    # def display(self):
    #     for row in range(self.height):
    #         for col in range(self.width):
    #             print ("#", end='')
    #         print()
    def display(self):
        rec = ['#' * self.width for _ in range(self.height)]

        for y in range(self.y):
            print(" " * self.y)

        for item in rec:
                print(" " * self.x, end='')
                print(item)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        if args:
            attr = ["id", "width", "height", "x", "y"]
            for idx, value in enumerate(args):
                if idx < len(attr):
                    setattr(self, attr[idx], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
