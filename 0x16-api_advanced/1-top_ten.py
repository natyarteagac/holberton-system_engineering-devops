#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests
import sys


def top_ten(subreddit):
    """ Return the top 10 """
    headers = {
        "User-Agent": "Mozilla/5.0:APIrequest1.0 (by u/natyarteagac)"
    }
    r = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.
        format(subreddit), headers=headers, allow_redirects=False)
    if str(r) != '<Response [200]>':
        return None
    else:
        response_json = r.json()
        title_name = response_json.get('data').get(
            'children')
        for index in range(0, 10):
            print(title_name[index].get('data').get('title'))
