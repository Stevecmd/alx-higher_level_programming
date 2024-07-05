#!/usr/bin/python3
"""
This script lists the 10 most recent commits of a given GitHub repository.
It requires the repository name and the owner's username as command-line
arguments.

Usage:
    The script requires two command-line arguments:
    1. Repository Name: The name of the repository from which to retrieve
       commits.
    2. Owner Name: The GitHub username of the repository's owner.

Dependencies:
    This script depends on the 'requests' library to send the GET request to
    the GitHub API.
    Ensure that 'requests' is installed in your environment before running
    this script.

Example:
    $ python3 100-github_commits.py rails rails
    This will list the 10 most recent commits from the 'rails' repository
    owned by the user 'rails'.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
