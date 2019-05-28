if __name__ == '__main__':
	n = int(input())
	a = "".join(str(x) for x in list(range(n+1)) if x!=0)
	print (a)