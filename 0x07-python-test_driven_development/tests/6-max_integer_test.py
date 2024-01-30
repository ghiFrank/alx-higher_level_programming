#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([5, 65, 18, 98, 20]), 98)
        self.assertEqual(max_integer([15, 95, 21, 69, 91]), 95)
        self.assertEqual(max_integer([65, 18, 25, 4, 46]), 65)

if __name__ == '__main__':
    unittest.main()
