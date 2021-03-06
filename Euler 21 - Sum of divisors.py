# Euler #21
# Sum of all numbers d(a) = b and d(b) = a where d(x) is the sum of divisors of x and a!=b

#returns a list of all divisors 
def all_divisors(n):				#from Euler12
	i=2
	divisors=[1]
	if n==0:return()
	elif n==1:return([1])
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

result=0

for number in range(10000):
	list1=all_divisors(number)
	sum1=sum(list1)
	list2=all_divisors(sum1)
	sum2=sum(list2)
	if number==sum2 and number!=sum1:
		result+=number

print(result)
