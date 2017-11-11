# Euler 35
# Sum of all numbers where the sum of factorials of single digits equals the number

import math

sum=0
result=0

for i in range(3,10000000):
	sum=0
	for numbers in range(len(str(i))):
		sum+=math.factorial(int(str(i)[int(numbers)]))
		if sum>i: break
	if sum==i:
		result+=sum 

print(result)

"""
[int(reduce(lambda x, y: int(x) + int(y), [str(reduce(lambda x, y: x * y, range(1, int(i) + 1) + [1])) for i in str(j)])) for j in range(0, 100000) if (j == int(reduce(lambda x, y: int(x) + int(y), [str(reduce(lambda x, y: x * y, range(1, int(i) + 1) + [1])) for i in str(j)])))]
"""