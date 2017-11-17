number=0
count=0
countmax=0
Schleife=True

while Schleife==True:
	#print(number)
	count=0
	number=number+1
	for i in range(1,21):
		if number%i==0:
			count=count+1
			if count>countmax:
				print (str(count)+ " bei "+str(number))
				countmax=count
			if count==20:
				Schleife=False					
		
print(number)
