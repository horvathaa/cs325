#Suppose you are given two sets of n points, one set {p1, p2, . . . , pn} on the line y = 0 and the
#other set {q1, q2, . . . , qn} on the line y = 1. Suppose, p1  x < p2  x < . . . < pn  x (where pi  x
#is the X-coordinate of pi). Create a set of n line segments by connecting each point pi to the
#corresponding point qi. Suppose no three line segments intersect in a point.

import sys

def createArray():
    n = 0
    endstr = ""
    p1 = []
    q2 = []
    input = open("input.txt") #hardcoded, might need to change to command line arguments
    n = input.readline()
    p1 = input.readline()
    p1 = p1.split(",")
    for s in p1:
        endstr = s.replace('\r\n', "")
    p1.pop()
    p1.append(endstr)
    q1 = input.readline()
    q1 = q1.split(",")

    return p1, q1

def recurse(p1, q1):
    
    return

def main():
    p1 = []
    q1 = []
    p1, q1 = createArray()
    print p1
    print q1

main()
