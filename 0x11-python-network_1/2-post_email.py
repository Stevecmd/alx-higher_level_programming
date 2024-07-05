#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a POST request to the
URL with the email as a parameter, and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    argv = sys.argv
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
