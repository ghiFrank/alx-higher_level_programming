#!/usr/bin/python3
"""Square module"""
from rectangle import Rectangle

class Square(Rectangle):
    __nb_objects = 0
    """constructor"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get/set Square's size"""
        return (self.width)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """returns printable string representation of Square"""
        return ("[Rectangle] ({}) {}/{} - {}".format(
            self.id, self.x,self.y, self.width,))

    def update(self, *args, **kwargs):
        """updates Square's attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
