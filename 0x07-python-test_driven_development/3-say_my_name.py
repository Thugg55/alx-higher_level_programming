#!/usr/bin/python3
# Edogun ...
""" function prints my name """


def say_my_name(first_name, last_name=""):
    """
    Args:
    First_name: String contains first name.
    Second_name: String contains second name.

    Raises:
    TypeError: If Args ain't strings
    """
    error = "first_name must be a string or last_name must be a string"
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError(error)
    print("My name is {} {}".format(first_name, last_name))
