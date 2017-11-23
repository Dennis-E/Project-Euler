# Euler Problem 47
# Find the first four four-digit numbers that have distinct prime factors

def prime_factors(n):
	i=2
	factors=[]
	if n==0:return()
	if n==1:return(1)
	while True:
		if n==1:
			return(factors)
		elif n%i==0:
			factors.append(i)
			n/=i
		else:
			i+=1

i=999

while True:
	i+=1
	factors=set()
	for element in prime_factors(i):
		factors.add(element)
	if len(factors)==4:
		factors=set()
		for element in prime_factors(i+1):
			factors.add(element)
		if len(factors)==4:
			factors=set()
			for element in prime_factors(i+2):
				factors.add(element)
			if len(factors)==4:
				factors=set()
				for element in prime_factors(i+3):
					factors.add(element)
				if len(factors)==4:
					print(i)
					break