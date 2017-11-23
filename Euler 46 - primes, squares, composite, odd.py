# Euler Problem 46
# Finding the first odd composite number that can not be written as the sum of a prime and 2*a square
# Composite numbers are positive integers that are not prime

def is_prime(number):
    max_value=int(number**(1/2)+1)
    if number==0 or number==1: return False
    if number==2: return True
    for i in range(2,max_value): #improved to only count until sqrt of number
        if number%i==0:
            return False
            break
    return True

i=1
primes=[]

while True:
	i+=1
	flag=True
	if is_prime(i)==False:
		if i%2!=0:										#only add composite numbers
			for prime in primes:
				for factor in range(int(i/2)):
					if prime+2*factor**2==i: flag=False
			if flag==True:
				print(i)
				break
	else:
		primes.append(i)
			