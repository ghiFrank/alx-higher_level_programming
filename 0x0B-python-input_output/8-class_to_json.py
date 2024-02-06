#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
