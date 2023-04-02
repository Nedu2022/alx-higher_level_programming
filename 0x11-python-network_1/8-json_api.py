#!/usr/bin/python3
"""Script to format json response
"""
import requests
import sys


def format_json():
    """Format JSON response as
    required
    """
    try:
        url = "http://0.0.0.0:5000/search_user"
        q = ""
        if len(sys.argv) > 1:
            q = sys.argv[1]

        res = requests.post(url, {"q": q})
        body = res.json()

        if len(body) == 0:
            print("No result")
        else:
            print(f"[{body.get('id')}] {body.get('name')}")
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    format_json()
