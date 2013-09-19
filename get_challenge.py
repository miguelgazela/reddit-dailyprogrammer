#!/usr/bin/env python

import requests
import webbrowser
import re
from bs4 import BeautifulSoup

BASE_URL = "http://www.reddit.com/r/dailyprogrammer/new/"

def get_soup(url):
    html = requests.get(url).text
    return BeautifulSoup(html)


def get_page_challenges(soup):
    return [challenge for challenge in soup.find_all('div', class_='thing')]


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
            'difficulty': result.group(2),
            'title': result.group(0)
        }

        challenges.append(challenge)

    return challenges


def main():
    page_challenges = get_page_challenges(get_soup(BASE_URL))
    challenges = build_challenges(page_challenges)
    for c in challenges:
        print c

if __name__ == "__main__":
    main()