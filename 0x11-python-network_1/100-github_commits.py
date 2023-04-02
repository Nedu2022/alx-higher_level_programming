#!/usr/bin/python3
"""Query GitHub API for commits
"""
import requests
import sys


def get_commits():
    """Query GitHub API for commits
    """
    try:
        repo, ownr = sys.argv[1:]
        url = f"https://api.github.com/repos/{ownr}/{repo}/commits?per_page=10"
        res = requests.get(url)
        body = res.json()
        for res in body:
            print(f"{res['sha']}: {res['commit']['author']['name']}")
    except Exception:
        pass


if __name__ == "__main__":
    get_commits()
