#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """defines a Rectangle"""

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle
        Args:
            width: rectangle's width
            heigth: rectangle's height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get/set rectangle's width"""
        return (self.__width)

    @property
    def height(self):
        """get/set rectangle's height"""
        return (self.__height)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return rectangle's area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """return rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns printable string representation of rectangle"""
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.height)

    def __del__(self):
        """Print a message for every deletion of a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger of two rectangles
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeErorr: if rect_1 or rect_2 are not instances of Rectangle.
        Returns:
        The rectangle with the larger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
