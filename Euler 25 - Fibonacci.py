# Euler 25
# Finding out which x for Fibonacci(x) has 1000 digits

number1=1
number2=1
i=2

while True:
	i+=1
	number3=number1+number2
	number1=number2
	number2=number3
	if len(str(number3))==1000:
		break

print(i)

"""
i, j, term = 0, 1, 2
i, j, term = j, fib, term+1
"""
