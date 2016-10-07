#Suppose you are given two sets of n points, one set {p1, p2, . . . , pn} on the line y = 0 and the
#other set {q1, q2, . . . , qn} on the line y = 1. Suppose, p1  x < p2  x < . . . < pn  x (where pi  x
#is the X-coordinate of pi). Create a set of n line segments by connecting each point pi to the
#corresponding point qi. Suppose no three line segments intersect in a point.

import sys

def createArray():
#%%^%%v0
    n = 0
    endstr = ""
    p1 = []
    q2 = []
    input = open("input.txt") #hardcoded, might need to change to command line arguments
    n = input.readline()
#^^%^^
    newN = n.replace('\r\n', "")
    p1 = input.readline()
    p1 = p1.split(",")
    for s in p1:
        endstr = s.replace('\r\n', "")
    p1.pop()
    p1.append(endstr)
    q1 = input.readline()
    q1 = q1.split(",")

    return newN, p1, q1

def recurse(n, p1, q1):
    #while(n > 0):
    for i in len(range(p1)):
        for j in len(range(p1)):
            if i != j:
                absuidbaidu
            if(q[i] > p[i]):
                if(p[i] < p[j] && q[i] > q[j]):
                    cross+=1
                    
    #return

def main():
    n = 0
    p1 = []
    q1 = []
    n, p1, q1 = createArray()
    print n
    print p1
    print q1

main()
