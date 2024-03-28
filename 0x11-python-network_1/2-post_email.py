#!/usr/bin/python3
"""Script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response"""
import sys
from urllib import parse
from urllib import request


if __name__ == "__main__":
    url = sys.argv[1]
    integer = {"email": sys.argv[2]}
    information = parse.urlencode(integer).encode("ascii")

    req = request.Request(url, information)
    with request.urlopen(reuqest) as response:
        res = response.read()
        print(res.decode("utf-8"))
