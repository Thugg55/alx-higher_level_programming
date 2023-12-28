#!/usr/bin/python3
# program prints numbers from 0 to 98

for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
