#!/usr/bin/python3
""" Defines a class rectangle """

class Rectangle:
    """ representation of a rectangle """
    
    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")  # Correct error message
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # Correct error message
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
