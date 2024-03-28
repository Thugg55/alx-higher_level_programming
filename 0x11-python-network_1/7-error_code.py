#!/usr/bin/python3
"""Script take in URL, sends a request to URL and 
displays the body of the response"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    fetch = request.get(url)
    if fetch.status_code >= 400:
        print("Error code: {}".format(fetch.status_code))
    else:
        print(fetch.text)
