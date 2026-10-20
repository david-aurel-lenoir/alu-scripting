#!/usr/bin/python3
"""Recursively collect the titles of all hot posts of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu.api_advanced:v1.0"}


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot post titles, or None if invalid."""
    if after is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        res = requests.get(url, headers=HEADERS, params=params,
                           allow_redirects=False, timeout=10)
    except Exception:
        return None
    if res.status_code != 200:
        return None
    data = res.json().get("data", {})
    hot_list = hot_list + [c.get("data", {}).get("title")
                           for c in data.get("children", [])]
    nxt = data.get("after")
    if nxt is None:
        return hot_list
    return recurse(subreddit, hot_list, nxt)
