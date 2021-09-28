#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and
returns a list containing the titles
"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=""):
    """Return the len of answers"""
    headers = {
        "User-Agent": "Mozilla/5.0:APIrequest1.0 (by u/natyarteagac)"
    }
    r = requests.get(
        'https://www.reddit.com/r/{}/hot.json?limit=50&after={}'.
        format(subreddit, after), headers=headers, allow_redirects=False)
    if str(r) != '<Response [200]>':
        return None
    else:
        after = r.json().get('data').get('after')
        if after is not None:
            response_json = r.json()
            title_name = response_json.get('data').get(
                'children')
        for index in range(0, 50):
            hot_list.append(title_name[index].get('data').get('title'))
        recurse(subreddit, hot_list, after)
    return(hot_list)
