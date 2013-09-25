#!/usr/bin/env python

# [08/06/13] Challenge #134 [Easy] N-Divisible Digits
# url: http://www.reddit.com/r/dailyprogrammer/comments/1jtryq/080613_challenge_134_easy_ndivisible_digits/


def main():
    n, m = map(int, raw_input().split())
    
    i = 10**n - 1
    result = None

    while i > 0:
        if i % m == 0:
            result = i
            break
        i -= 1

    if result:
        print result

    """
    or
    i = 10**n - 1
    result = i - i % m
    return result
    """


if __name__ == "__main__":
    main()

