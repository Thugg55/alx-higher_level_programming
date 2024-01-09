#!/usr/bin/python3
# replaces an element of a list
# Edogun ...

def replace_in_list(my_list, idx, element):
    if idx < o or idx > len(my_list):
        return(my_list)
    else:
        my_list[idx] = element
        return(my_list)
