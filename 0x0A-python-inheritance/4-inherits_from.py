#!/usr/bin/python3
'''Module For inherits_from'''


def inherits_from(obj, a_class):
    '''Checks if the object is an instance of a class
        that inherited from the specified class.
    Args:
        obj (object): the object.
        a_class: the class.
    Returns:
        True: if the object is an instance of a class
            that inherited from the specified class
        False:
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
