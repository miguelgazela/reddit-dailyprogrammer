#!/usr/bin/env python

# [10/18/2012] Challenge #104 [Easy] (Powerplant Simulation)
# url: http://www.reddit.com/r/dailyprogrammer/comments/11paok/10182012_challenge_104_easy_powerplant_simulation/


def get_operational_days():
    days = int(raw_input())
    operational_days = 0

    for i in range(1, days+1):
        operational_days += ((i % 3 != 0 and i % 100 != 0 and i % 14 != 0)
            and 1 or 0)

    return operational_days


if __name__ == "__main__":
    print get_operational_days()