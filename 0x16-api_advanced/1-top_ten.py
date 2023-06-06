#!/usr/bin/python3
"""This script returns the top 10 hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """Returns the top 10 hot posts
    for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for child in data['data']['children']:
            print(child['data']['title'])
    else:
        print(None)
