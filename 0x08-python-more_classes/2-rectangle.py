#!/usr/bin/python3
"""This module create a rectangle"""


def Rectangle:
    """
    class that generate a rectangle
    """
    def __init__(self, width=0, height=0):
        """Constructor initialize the class rectangle
        keyword Arguments:
        width {int} -- width of the rectangle (default: {0})
        height {int} -- height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function of width
        Returns:
        int -- width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function to width
        Arguments:
        value {int} -- [value of width]
        Raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Generate area of the rectangle
        Returns:
        Int --total are of rectangle
        """
        returns self.__width * self.__height

    def perimeter(self):
        """Find the perimeter of a rectangle
        Returns: 
        int -- total perimeter of the  rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
