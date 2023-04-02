#!/usr/bin/python3
"""
Script to fetch https://alx-intranet.hbtn.io/status
"""
import urllib.request


def fetch():
    """Fetch data from the an endpoint
    """
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf8')}")


if __name__ == "__main__":
    fetch()
