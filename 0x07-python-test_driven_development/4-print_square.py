#!/usr/bin/python3
# Edogun ...
""" function prints a square """

def print_square(size):
    """
    Args:
    size: size length of the square

    Raises:
    TypeError: If size isn't an integer
    ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
