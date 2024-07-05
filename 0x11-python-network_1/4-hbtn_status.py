#!/usr/bin/python3
"""
This script fetches the status from 'https://alx-intranet.hbtn.io/status'
using the 'requests' package. It prints the type and content of the response
body in a formatted manner.
"""

import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
