#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu.api_advanced:v1.0"}


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    response = requests.get(url, headers=HEADERS, params={"limit": 10},
                            allow_redirects=False)
    if response.status_code in (301, 302, 404):
        print(None)
        return
    try:
        children = response.json().get("data").get("children")
    except Exception:
        print(None)
        return
    if not children:
        print(None)
        return
    for child in children[:10]:
        print(child.get("data").get("title"))
