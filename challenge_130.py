#!/usr/bin/env python

# [06/17/13] Challenge #130 [Easy] Roll the Dies
# url: http://www.reddit.com/r/dailyprogrammer/comments/1givnn/061713_challenge_130_easy_roll_the_dies/

import random

def main():
    n, m = map(int, raw_input().split('d'))[:2]
    
    for __ in range(n):
        print random.randint(1, m),

if __name__ == "__main__":
    main()

