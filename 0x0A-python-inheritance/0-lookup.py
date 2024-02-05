#!/usr/bin/python3
'''Module For lookup'''


def lookup(obj):
    '''Looks for available attributes and methods of an object.
    Args:
        obj (object): the object.
    Returns:
        List: the list of attributes
    '''
    return dir(obj)
