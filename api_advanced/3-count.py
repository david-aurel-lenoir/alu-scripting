#!/usr/bin/python3
"""Recursively count keywords in the hot post titles of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu.api_advanced:v1.0"}


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the given keywords in hot post titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        res = requests.get(url, headers=HEADERS, params=params,
                           allow_redirects=False, timeout=10)
    except Exception:
        return
    if res.status_code != 200:
        return
    data = res.json().get("data", {})
    for child in data.get("children", []):
        title = child.get("data", {}).get("title", "").lower().split()
        for key in counts:
            counts[key] += title.count(key)
    nxt = data.get("after")
    if nxt is not None:
        return count_words(subreddit, word_list, nxt, counts)
    totals = {}
    for word in word_list:
        key = word.lower()
        totals[key] = totals.get(key, 0) + counts.get(key, 0)
    for key, value in sorted(totals.items(), key=lambda kv: (-kv[1], kv[0])):
        if value > 0:
            print("{}: {}".format(key, value))
