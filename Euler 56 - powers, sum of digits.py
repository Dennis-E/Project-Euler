# Euler Problem 56
# Biggest sum of digits in a**b for a and b below 100

def sum_of_digits(n):
	digits=[]
	for i in range(len(str(n))):
		digits.append(int(str(n)[i]))
	return sum(digits)

maximum=0

for a in range(1,100):
	for b in range(1,100):
		if sum_of_digits(a**b)>maximum: maximum=sum_of_digits(a**b)

print(maximum)