#!/usr/bin/python3
"""This script returns the hot posts for a given subreddit recursively"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns the hot posts
    for a given subreddit recursively"""
    if hot_list is None:
        hot_list = []

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'after': after} if after else None

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for child in data['data']['children']:
            hot_list.append(child['data']['title'])

        after = data['data']['after']

        if after:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
    else:
        return None
