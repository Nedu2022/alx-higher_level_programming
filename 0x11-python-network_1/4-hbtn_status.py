#!/usr/bin/python3
"""
Script to fetch https://alx-intranet.hbtn.io/status
using python requests package
"""
import requests


def fetch():
    """Fetch data from the an endpoint
    using the requests package
    """
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")


if __name__ == "__main__":
    fetch()
