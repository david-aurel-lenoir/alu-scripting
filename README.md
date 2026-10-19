# API Advanced

A collection of Python scripts that query the Reddit API, covering pagination,
recursion, and JSON parsing, as part of the ALU Higher Level Programming
curriculum.

## Learning Objectives

By the end of this project, you should be able to explain:

- How to read API documentation to find the right endpoints
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Requirements

- Python 3.4.3 (Ubuntu 14.04 LTS)
- PEP 8 style
- Requests module for HTTP calls
- Custom User-Agent header required for Reddit API
- No redirects allowed (allow_redirects=False)

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-subs.py` | Return subscriber count for a subreddit |
| 1 | `1-top_ten.py` | Print titles of top 10 hot posts |
| 2 | `2-recurse.py` | Recursively get all hot post titles |
| 3 | `3-count.py` | Recursively count keyword occurrences in hot titles |
