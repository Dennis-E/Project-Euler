# Euler 23
# Part 1
# Create a file with all abundant numbers <=28123

j=0
divisors=[]

def all_divisors(n):				#v 3.0 based on and radically simplified from Euler21, avoiding root of all evil of premature optimization (http://wiki.c2.com/?PrematureOptimization)
	divisors=[]
	if n==0:return([])
	for i in range(1,n):
		if n%i==0:
			divisors.append(i)
	return divisors

with open(r"C:\Users\user\workspace\Euler\list_of_abundant_numbers.txt","w") as F:
	for i in range(1,28124):	#28124
		if sum(all_divisors(i))>i:
			j=j+1
			F.write(str(i)+", ")
