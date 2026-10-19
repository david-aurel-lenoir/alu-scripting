#!/usr/bin/python3
"""Module that counts keyword occurrences in Reddit hot post titles."""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Print sorted count of keywords found in hot post titles."""
    if not counts:
        counts = {word.lower(): 0 for word in word_list}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/stephane_alu)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1
    next_after = data.get("after")
    if next_after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return
    return count_words(subreddit, word_list, counts, next_after)
