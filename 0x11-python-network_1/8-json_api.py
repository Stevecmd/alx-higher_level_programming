#!/usr/bin/python3
# This script takes in a letter, sends a POST request to a specified URL with
# the letter as a parameter, and handles the response.

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(
        'http://0.0.0.0:5000/search_user',
        data={'q': q}
    )

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(
                json_response.get('id'), json_response.get('name')
            ))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
