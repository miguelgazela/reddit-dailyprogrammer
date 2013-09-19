#!/usr/bin/env python

# [09/17/13] Challenge #138 [Easy] Repulsion-Force
# url: http://www.reddit.com/r/dailyprogrammer/comments/1ml669/091713_challenge_138_easy_repulsionforce/

import math

class Particle(object):

    def __init__(self, mass=0.0, x=0.0, y=0.0):
        self.mass = mass
        self.x = x
        self.y = y

    def distance_to(self, p):
        delta_x = self.x - p.x
        delta_y = self.y - p.y
        return math.sqrt(delta_x**2 + delta_y**2)

    def force_between(self, p):
        return (self.mass * p.mass) / (self.distance_to(p)**2)


def get_values():
    return [float(x) for x in raw_input().split()]


def main():

    p1 = get_values()
    p2 = get_values() 

    p1 = Particle(p1[0], p1[1], p1[2])
    p2 = Particle(p2[0], p2[1], p2[2])

    print "%.4f" % p1.force_between(p2)

if __name__ == "__main__":
    main()

