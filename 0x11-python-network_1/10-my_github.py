#!/usr/bin/python3
"""Script makes request to GitHub API
for user id
"""
import requests
import sys


def get_profile_id():
    """Query GitHub API to get user id
    """
    url = "https://api.github.com/user"

    username, password = sys.argv[1:]

    res = requests.get(
        url, headers={"Authorization": f"Bearer {password}"})

    if res.status_code == 200:
        body = res.json()
        print(body.get('id'))
    else:
        print("None")


if __name__ == "__main__":
    get_profile_id()
