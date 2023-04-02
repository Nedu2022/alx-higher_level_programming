#!/usr/bin/python3
"""Script make request to a url with error
    handling included using python requests package
"""
import requests
import sys


def fetch():
    """Make request to a url and handle
    errors if any
    """
    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)


if __name__ == "__main__":
    fetch()
