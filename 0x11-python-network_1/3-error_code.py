#!/usr/bin/python3
"""Script make request to a url with
error handling included
"""
from urllib import request, error
import sys


def fetch():
    """Make request to a url and handle
    errors if any
    """
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf8"))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    fetch()
