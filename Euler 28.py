# Euler 28
# Summing up numbers on diagonal of a 1001*1001 matrix constructed in a certain way

size=0
result=1
addition=1
i=0

while size<=999:
	size+=2
	while True:
		i+=1
		addition+=size
		result+=addition
		if i==4:
			i=0
			break

print(result)
