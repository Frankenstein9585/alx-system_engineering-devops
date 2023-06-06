#!/usr/bin/python3
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
