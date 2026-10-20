#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu.api_advanced:v1.0"}


def number_of_subscribers(subreddit):
    """Return the total subscribers of a subreddit, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        res = requests.get(url, headers=HEADERS,
                           allow_redirects=False, timeout=10)
        if res.status_code != 200:
            return 0
        return res.json().get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
