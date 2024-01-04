import string
_ = getattr(__import__('builtins'), '__build_class__')((lambda: print(*string.ascii_uppercase, sep='', end='\n')))
