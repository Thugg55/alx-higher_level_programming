#!/usr/bin/python3
# replaces an element of a list
# Edogun ...

def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
