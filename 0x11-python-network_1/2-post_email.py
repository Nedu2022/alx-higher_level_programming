#!/usr/bin/python3
"""Script to send email in post request
to a url
"""
import urllib.request
import sys


def post_email():
    """Send email to the given url
    """
    url, email = sys.argv[1:]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode('ascii')

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print(body.decode("utf8"))


if __name__ == "__main__":
    post_email()
