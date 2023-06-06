#!/usr/bin/python3
"""This script returns the hot posts for a given subreddit recursively"""
import requests


def recurse(subreddit):
    """Returns the hot posts
    for a given subreddit recursively"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        hot_list = []
        for child in data['data']['children']:
            hot_list.append(child['data']['title'])

        after = data['data']['after']

        if after:
            return recurse(subreddit)
        else:
            return hot_list
    else:
        return None
