#!/usr/bin/python3
# checks for lowercase
# Edogun ...

def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
