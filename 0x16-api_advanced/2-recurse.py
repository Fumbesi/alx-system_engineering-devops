#!/usr/bin/python3
"""
2-recurse
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API to get the titles of all hot articles for a subreddit.

    :param subreddit: The name of the subreddit.
    :param hot_list: A list to store the titles (default is an empty list).
    :param after: A token for pagination (default is None).
    :return: A list of titles or None if the subreddit is invalid or has no hot articles.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            if not hot_list:
                return None
            else:
                return hot_list

        hot_list.extend([post["data"]["title"] for post in posts])
        after = data["data"]["after"]

        return recurse(subreddit, hot_list, after)
    else:
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        hot_titles = recurse(subreddit)

        if hot_titles is not None:
            print(len(hot_titles))
        else:
            print("None")
