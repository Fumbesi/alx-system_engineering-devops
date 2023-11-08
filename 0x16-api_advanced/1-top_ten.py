#!/usr/bin/python3
"""
1-top_ten
"""

import requests

def top_ten(subreddit):
    """
    Query the Reddit API to print the titles of the first 10 hot posts for a subreddit.

    :param subreddit: The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if posts:
            for post in posts:
                print(post["data"]["title"])
        else:
            print("No hot posts found in this subreddit.")
    else:
        print(None)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
