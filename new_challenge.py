#!/usr/bin/env python

import requests
import webbrowser
import re
import os
import sys
from bs4 import BeautifulSoup


BASE_URL = "http://www.reddit.com/r/dailyprogrammer/new/"


def get_soup(url):
    return BeautifulSoup(requests.get(url).text)


def get_page_challenges(soup):
    return [challenge for challenge in soup.find_all('div', class_='thing')]


def get_completed_challenges():
    regex = re.compile("^challenge_(\d{1,}).py$")
    return [f[10:-3] for f in os.listdir(os.getcwd()) if regex.match(f)]


def build_challenges(page_challenges):
    challenges = []
    regex = re.compile("^.{21}#(\d{1,}) \[([a-zA-Z]{4,12})\] (.+)$")

    for page_challenge in page_challenges:
        title = page_challenge.find('a', class_='title')
        result = regex.match(title.text)

        if result is None:
            continue

        challenge = {
            'fullname': page_challenge.get('data-fullname'),
            'name': result.group(3),
            'number': result.group(1),
            'url': title.get('href'),
            'difficulty': result.group(2).lower(),
            'title': result.group(0)
        }

        challenges.append(challenge)

    return challenges


def main():

    if len(sys.argv) != 2:
        print "Usage: new_challenge.py <difficulty>"
        exit(-1)

    difficulty = sys.argv[1]

    if difficulty.lower() not in ['easy', 'intermediate', 'hard']:
        print "Invalid type of difficulty. "\
            "Available choices: easy, intermediate or hard."
        exit(-1)

    # process completed files and get new challenges from reddit
    completed = get_completed_challenges()
    page_challenges = get_page_challenges(get_soup(BASE_URL))

    # chooses the first one that hasn't been completed
    while True:
        challenges = build_challenges(page_challenges)

        if not challenges:
            print "No challenges found!"
            exit()

        for c in challenges:
            if c['number'] not in completed and c['difficulty'] == difficulty:
                print c
                webbrowser.open_new("".join([
                    "http://www.reddit.com",
                    c['url']]))
                exit()

        # no challenges available in the current page, go to next page
        page_challenges = get_page_challenges(get_soup("".join(
            [BASE_URL,
            "?count=",
            str(len(page_challenges)),
            "&after=",
            challenges[len(challenges)-1]['fullname']
        ])))


if __name__ == "__main__":
    main()