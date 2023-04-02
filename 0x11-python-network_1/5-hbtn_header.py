#!/usr/bin/python3
"""Script takes in a url, make a request to the url
and prints X-Request-Id response header
"""
import requests
import sys


def print_header():
    """Display X-Request-Id response header
    """
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))


if __name__ == "__main__":
    print_header()
