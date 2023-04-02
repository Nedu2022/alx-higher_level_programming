#!/usr/bin/python3
"""Script to send email in post request
to a url using python requests package
"""
import requests
import sys


def post_email():
    """Send email to the given url
    using python requests package
    """
    url, email = sys.argv[1:]
    res = requests.post(url, {"email": email})
    print(res.text)


if __name__ == "__main__":
    post_email()
