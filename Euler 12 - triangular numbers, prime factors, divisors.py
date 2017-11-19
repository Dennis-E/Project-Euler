# Euler problem 12
# 

def check_triangle(n):
	i=0
	remainder=n
	while True:
		i+=1
		remainder-=i
		if remainder==0:
			return True
			break
elif remainder<0:
			return False
			break

# Returns a list of the prime factors of the input number "n"
def prime_factors(n):
	i=2
	primes=[]
	while True:
		if n%i==0:
			n=n/i
			primes.append(i)
		elif n==1:
			return primes
		else:
			i+=1

#returns a list of all divisors
def all_divisors(n):			
	i=2
	divisors=[1]
	if n==1:return([1])
	elif n==2:return([1,2])
	else:
		while True:
			if n%i==0:
				if i in divisors:
					return divisors
				divisors.append(i)
				divisors.append(int(n/i))	
				i+=1
			elif i>n:
				return divisors
			else:
				i+=1

i=0
n=0
max=0

while True:
	i+=1
	n+=i
	if len(all_divisors(n))>max:
		max=len(all_divisors(n))
		print(n)
		print(max)
		print(all_divisors(n))
	if max>500: break
