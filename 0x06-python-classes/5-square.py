#!/usr/bin/python3
"""square module"""


class Square:
		"""defines a square"""
		def __init__(self, size=0):
			"""constructor
			Args:
				size: length of a side of the square
			"""
			self.__size = size

		@property
		def size(self):
			"""property for the length of side of the square
			Raises:
				TypeError: if size is not an integer
				ValueError: if size is less than 0
			"""
			return self.__size

		@size.setter
		def size(self, value):
			if not isinstance(value, int):
				raise TypeError('size must be an integer')
			if value < 0:
				raise ValueError('size must be >=0')
			self.__size = value

		def area(self):
			"""Area of this square
			Returns:
				The size squared
			"""
			return self.__size ** 2
		def my_print(self):
			if self.__size == 0:
				print()
			for n in range(0, self.__size):
				for i in range(0, self.__size):
					print('#', end="")
				print()
