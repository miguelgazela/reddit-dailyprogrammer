#!/usr/bin/env python

# [07/01/13] Challenge #131 [Easy] Who tests the tests?
# url: http://www.reddit.com/r/dailyprogrammer/comments/1heozl/070113_challenge_131_easy_who_tests_the_tests/

def reverse_str(string):
    return string[::-1]


def str_to_upper(string):
    return string.upper()


def main():
    n = int(raw_input())
    tests = [raw_input().split() for __ in range(n)]

    for test in tests:
        if int(test[0]) == 0:
            print (reverse_str(test[1]) == test[2] and 
                "Good test data" or "Mismatch! Bad test data")
        elif int(test[0]) == 1:
            print (str_to_upper(test[1]) == test[2] and
                "Good test data" or "Mismatch! Bad test data")

if __name__ == "__main__":
    main()

