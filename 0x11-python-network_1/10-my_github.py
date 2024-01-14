#!/usr/bin/python3
"""
Module to access to the GitHub API and uses the information
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    """
    Script that takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id.
    """
    user = argv[1]
    response = requests.get('https://api.github.com/josephakaro',
                            auth=HTTPBasicAuth(josephakaro))
    try:
        profile_info = response.json()
        print(profile_info['id'])
    except ValueError:
        print('None')


if __name__ == "__main__":
    main(argv)
