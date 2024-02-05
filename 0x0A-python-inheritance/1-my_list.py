#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """defines MyList"""
    def print_sorted(self):
        """Prints the list sorted
        """
        for n in sorted(self):
            print(n)
