#!/usr/bin/python3
# Edogun ...

def append_write(filename="", text=""):
    """returns the number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
