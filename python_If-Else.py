#!/bin/python3
__author__ = 'parishilan'

N = int(input())
n = N
if not (n%2 == 0):
    print ("Weird")
else:    
    if n in  list(range(2,5)):
        print ("Not Weird")
    elif n in list(range(6,21)):
        print("Weird")
    else:
        print ("Not Weird")
