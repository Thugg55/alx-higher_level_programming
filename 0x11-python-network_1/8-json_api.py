#!/usr/bin/python3
"""Script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""

import requests
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        url = ""
    peter = {'url': url}
    fetch = requests.post{'http://0.0.0.0:5000/search_user', data = peter)
    try:
        if r.json() == {}:
            print('No result')
        else:
            print('[{}] {}'.format(info.get('id'), info.get('name')))
    except ValueError:
        print('Not a valid JSON')
