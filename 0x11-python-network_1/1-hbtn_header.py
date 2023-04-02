#!/usr/bin/python3
"""Script to print X-Request-Id response header
"""
import urllib.request
import sys


def print_header():
    """Display X-Request-Id response header
    """
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))


if __name__ == "__main__":
    print_header()
