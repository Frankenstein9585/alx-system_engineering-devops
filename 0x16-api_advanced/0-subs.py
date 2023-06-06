#!/usr/bin/python3
"""This script returns the number of subscribers
    for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers
    for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    return 0
