#!/usr/bin/python3
# program imports functions from the file calculator_1
# Edogun ...

if __name__ == "__main__":
    """print the results of some maths performed on imported functions"""
    from calculator_1 import *

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} // {} = {}".format(a, b, div(a, b)))
