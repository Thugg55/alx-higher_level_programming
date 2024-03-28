#!/usr/bin/python3
"""Script displays the X-Request_Id header variable of a request 
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    x = urllib.request.Request(url)
    with urllib.request.urlopen(x) as response:
        y = response.info()
        print('{}'.format(y.get('X-Request-Id')))
