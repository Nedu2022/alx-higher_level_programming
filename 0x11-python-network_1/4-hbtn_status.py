#!/usr/bin/python3
"""
     Fetches https:alx-intranet.hbtn.io/status using requests
"""
import requests


if __name__ == "__main__":
    read_url = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(read_url.text))
    print("\t- content:", read_url.text)
