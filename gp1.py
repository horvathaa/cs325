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
    n = int(input.readline().rstrip('\n'))
    p1 = input.readline().rstrip('\n').split(",")
    q1 = input.readline().rstrip('\n').split(",")

    return n, p1, q1


def nLogN(n, p1):

    return



def recurse(n, p1, q1):
    cross = 0
    if(n > -1):
        cross = recurse(n - 1, p1, q1) 
        for i in range(n - 1):
            if(int(q1[n-1]) < int(q1[i])):
                cross+=1
    #print cross 
    return cross

def main():
    n = 0
    p1 = []
    q1 = []
    n, p1, q1 = createArray()
    print n
    print p1
    print q1
    print recurse(int(n), p1, q1)

main()
