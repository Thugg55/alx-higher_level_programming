#!/usr/bin/python3
"""Function fins a peak in a list of usorted integers"""


def find_peak(list_of_integers):
    """peak in a list of integers"""
    list_of_integers.sort()
    if (list_of_integers == []):
        return None
    else:
        return (list_of_integers[-1])
