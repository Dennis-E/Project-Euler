max=0

for i in range(1000000,0,-1):
	count=0
	n=i
	while n!=1:
		if n%2==0:
			n=1/2*n
		else:
			n=3*n+1
		count+=1
	if count>max:
		max=count
		starting_figure=i
		print(max)

print(starting_figure)
