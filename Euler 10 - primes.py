primelist=[]

for i in range(2,2000001):
	prime=True
	
	for j in primelist:			#Primfaktorzerlegung
		if i%j==0:
			prime=False
			break
			
	if prime==True:				#Check if prime
		primelist.append(i)
		print(str(i)+" is the "+str(len(primelist))+" prime")
	
	i+=1

print(sum(primelist))
	
