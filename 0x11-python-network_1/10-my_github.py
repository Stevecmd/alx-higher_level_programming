#!/usr/bin/python3
"""
This script uses the GitHub API to display the user's ID based on provided
GitHub credentials. It requires the user's username and a personal access
token as command-line arguments. The script utilizes Basic Authentication
to securely access user information. Only the 'read:user' permission is
necessary for the personal access token. It employs the requests package
for making HTTP requests and sys for accessing command-line arguments.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("None")
