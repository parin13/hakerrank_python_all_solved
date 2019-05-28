'''

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

'''


#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(raw_input())
n = 4

if not (n%2 == 0):
	print ("Weird")
else:	
	if n in  list(range(2,5)):
		print ("Not Weird")
	elif n in list(range(6,21)):
		print("Weird")
	else:
		print ("Not Weird")
