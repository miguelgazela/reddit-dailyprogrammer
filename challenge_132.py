#!/usr/bin/env python

# [07/08/13] Challenge #132 [Easy] Greatest Common Divisor
# url: http://www.reddit.com/r/dailyprogrammer/comments/1hvh6u/070813_challenge_132_easy_greatest_common_divisor/

def gcd(a, b):
    remainder = a % b

    if remainder == 0:
        return b
    else:
        return gcd(b, remainder)


def main():
    print gcd(8, 12)

if __name__ == "__main__":
    main()

