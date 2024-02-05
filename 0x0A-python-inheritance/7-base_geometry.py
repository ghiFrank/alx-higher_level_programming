#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry():
    """defines BaseGeometry"""

    def area(self):
        """Area of the bast geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Area of the bast geometry
            name: name of int
            value: value of int
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
