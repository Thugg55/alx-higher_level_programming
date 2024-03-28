#!/usr/bin/python3
""" Python script that fetches "https://alx-intranet.htbn.io/status """

import urllib.request


if __name__ == "__main__":
    req = request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("Body respomse:")
        print("\t- type: {}".format(type(page)))
        print("\t- content:", page)
        print("\t- utf8 content: {}".format(page.decode("utf-8")))
