#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes the square with a given size.

        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
