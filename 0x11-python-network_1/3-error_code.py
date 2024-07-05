#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body
of the response. It manages urllib.error.HTTPError exceptions and prints
"Error code:" followed by the HTTP status code. Only the packages urllib and
sys are used, adhering to the requirement of not importing other packages.
The script uses the with statement for efficient resource management.
"""

import sys
from urllib import request, error

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
