#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method for dictionary representation"""
        json_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int)):
                json_dict[key] = value
        return json_dict
