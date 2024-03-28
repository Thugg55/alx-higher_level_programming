#!/usr/bin/python3
"""Script takes in a URL and an email address, sends a POST request to the URL with 
the email as parameter, and finally displays the body of the response"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    integer = {"email": sys.argv[2]}

    fetch = requests.post(url, data=integer)
    print("{}".format(fetch.text))
