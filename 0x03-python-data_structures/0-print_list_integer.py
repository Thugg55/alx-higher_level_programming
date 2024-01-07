#!/usr/bin/python3
# prints all integers of a list
# Edogun ...

def print_list_integer(my_list=[]):
    for elements in range(len(my_list)):
        print("{:d}".format(my_list[elements]))
