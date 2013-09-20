#!/usr/bin/env python

# [09/17/13] Challenge #137 [Easy] Easy String Transposition
# url: http://www.reddit.com/r/dailyprogrammer/comments/1m1jam/081313_challenge_137_easy_string_transposition/

import sys

def main():
    n = int(raw_input())
    strings = [raw_input() for __ in range(n)]
    max_len = max(len(string) for string in strings)

    for i in range(max_len):
        for string in strings:
            if i > (len(string)-1):
                sys.stdout.write(" ")
            else:
                sys.stdout.write(string[i])
        print ""

if __name__ == "__main__":
    main()

