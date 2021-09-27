#!/usr/bin/python3
"""Function that queries the Reddit API and
returns the number of subscribers"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ Return the number of suscribers"""
    headers = {
        "User-Agent": "Mozilla/5.0:APIrequest1.0 (by u/natyarteagac)"
    }
    r = requests.get(
        'https://www.reddit.com/r/{}/about.json'.
        format(subreddit), headers=headers, allow_redirects=False)
    if str(r) != '<Response [200]>':
        return 0
    else:
        format_json = r.json()
        number_of_suscribers = format_json.get('data').get('subscribers')
        return number_of_suscribers
