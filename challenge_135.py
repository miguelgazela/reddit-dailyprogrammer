#!/usr/bin/env python

# [08/13/13] Challenge #135 [Easy] Arithmetic Equations
# url: http://www.reddit.com/r/dailyprogrammer/comments/1k7s7p/081313_challenge_135_easy_arithmetic_equations/

from sys import argv
import random


def main():
    script, n1, n2 = argv

    while True:
        equation = ""
        for __ in range(4):
            equation += "".join([
                str(random.randrange(int(n1), int(n2))),
                " ",
                random.choice(['+', '-', '*']),
                " "
            ])

        equation = equation[:-2]
        print equation

        user_answer = raw_input('>')
        result = eval(equation)

        if user_answer in "qQ":
            break
        elif int(user_answer) == result:
            print "Correct!"
        else:
            print "Incorrect."


if __name__ == "__main__":
    main()

