#!/usr/bin/python3
# Edogun ...

def print_reversed_list_integer(my_list=[]):
    """prints all integers of list in reversed order"""
    if my_list:
        for i in reversed(range(len(my_list))):
            print("{:d}".format(my_list[i]))
