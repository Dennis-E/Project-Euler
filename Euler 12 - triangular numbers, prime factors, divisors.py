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
	

"""			
number=0
i=0
max=0

while True:
	i+=1
	number+=i
	print(i)
	print(number)
	print(all_divisors(number))
	print("Triangle number "+str(number)+" has "+str(len(all_divisors(number)))+" factors")	
	if len(all_divisors(number))>500: break
"""
	
"""
	if number<(100000000**2/2):			#Smallest number of prime factors which combine to >500 factors, i.e. n*(n+1)/2>500
		print("smaller")
	else:
		if len(prime_factors(number))>max:
			max=len(prime_factors(number))
			print(max)
			if max>=32:
				print(len(all_divisors(number)))
				print(number)
				print(prime_factors(number))
				break
		
	if i%1000==0:
		print(i)
"""

""""
# no solution after 5 hours

i=0
triangle_number=0
counter=0
max=0

while True:
	i+=1
	triangle_number+=i
	for j in range(1,int(triangle_number/2)+1):	
		if triangle_number%j==0:		#Check if multiplicator
			counter+=1					#Count them
	
	if counter>max:
		max=counter
		print(max)
	
	if counter>500:
		break
	else:
		counter=0
		
print(triangle_number)
"""