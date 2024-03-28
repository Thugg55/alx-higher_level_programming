#!/usr/bin/python3
"""Script takes URL, sends a request to the URL and displays the body
"""
import sys
from urllib import error
from urllib import request


if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            uyi = response.read()
            print(uyi.decode("utf-8"))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
