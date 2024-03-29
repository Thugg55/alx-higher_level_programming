#!/usr/bin/python3
"""Script takes my Github credentails and uses Github API to display id"""

import sys
import requests


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = 'https://api.github.com/user'
    fetch = requests.get(url, auth=auth)
    print('{}'.format(fetch.json().get('id')))
