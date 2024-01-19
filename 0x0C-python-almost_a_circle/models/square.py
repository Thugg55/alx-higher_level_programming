#!/usr/bin/python3
# Edogun ...
""" function defines a square class that inherits from rectangle """

from models.Rectangle import Rectangle


class Square(Rectangle):
    """ introduces a class of Squar """

def __init__(self, size, x=0, y=0, id=None):
    """ definition initializes a new square """

    """
    Args:
    size: An int, represents the size of the new square
    x: An int, represents the x coordinate
    y: An int, represents the y coordinate
    id: An int, represents the new square
    """
    super().__init__(size, size, x, y, id)

