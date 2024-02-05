#!/usr/bin/python3
'''Module For lookup'''


def is_same_class(obj, a_class):
    '''Checks if the object is exactly an instance of the specified class.
    Args:
        obj (object): the object.
        a_class: the class.
    Returns:
        True: if the object is exactly an instance of the specified class
        False:
    '''
    if isinstance(obj, a_class) is True:
        return True
    return False
