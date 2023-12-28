#!/usr/bin/python3
# prints script in uppercase
# Edogun ...

def uppercase(str):
    for c in str:
        if 122 >= ord(c) >= 97 
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
