#!/usr/bin/python3
"""Script list the 10 most recent commits of a Github repo"""

import requests
import sys


if __name__ == "__main__":
    reponm = sys.argv[1]
    ownernm = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(ownernm, reponm)
    fetch = requests.get(url)
    commits = fetch.json()
    try:
        for j in range(10):
            print("{}: {}".format(
                commits[j].get("sha"),
                commits[j].get("commit").get("author").get("name")))
    except IndexError:
        pass
