#!/usr/bin/python3
"""
100-count
"""

import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively query the Reddit API to count keywords in the titles of hot articles.

    :param subreddit: The name of the subreddit.
    :param word_list: A list of keywords to count.
    :param after: A token for pagination (default is None).
    :param word_count: A dictionary to store word counts (default is an empty dictionary).
    """
    if not word_list:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            if not after:
                return

        for post in posts:
            title = post["data"]["title"]
            words = title.lower().split()

            for word in word_list:
                word = word.lower()

                if word in words and not title.endswith((".", "!", "_")):
                    word_count[word] = word_count.get(word, 0) + words.count(word)

        after = data["data"]["after"]
        count_words(subreddit, word_list, after, word_count)
    else:
        return

    if not after:
        sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_word_count:
            print(f"{word}: {count}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = sys.argv[2].split()
        count_words(subreddit, keywords)
