#!/usr/bin/python3
"""BaseGeometry module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass representing a Square."""
    def __init__(self, size):
        '''Constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method which returns area of Square.'''
        return self.__size ** 2

    def __str__(self):
        '''Returns string representation of this square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
