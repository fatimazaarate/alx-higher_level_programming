#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__( size, size, x, y, id)

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        attr = ["id", "size", "x", "y"]
        if args:
            for indx, value in enumerate(args):
                if indx < len(attr):
                    setattr(self, attr[indx], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    