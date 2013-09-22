#!/usr/bin/env python

# [08/13/13] Challenge #136 [Easy] Student Management
# url: http://www.reddit.com/r/dailyprogrammer/comments/1kphtf/081313_challenge_136_easy_student_management/

def calc_student_averages(records, m):
    averages = []
    for student in records:
        grades = map(int, student[1:])
        averages.append((student[0], sum(grades)/float(m)))
    return averages


def main():
    n, m = map(int, raw_input().split())
    records = [raw_input().split() for __ in range(n)]

    averages = calc_student_averages(records, m)
    class_average = sum([student[1] for student in averages])/float(n)

    for name, avg in averages:
        print "{0} {1:.2f}".format(name, avg)
    print "{0:.2f}".format(class_average)

if __name__ == "__main__":
    main()

