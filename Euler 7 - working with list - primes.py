i=1
primelist=[]

while True:
	i+=1						#Zu pruefende Zahl
	remainder=i
	
	for j in primelist:			#Primfaktorzerlegung
		if i%j==0:
			remainder=0
			break
			
	if remainder==i:			#Check if prime
		primelist.append(i)
		print(str(i)+" is the "+str(len(primelist))+" prime")
	
	if len(primelist)==10001:
		print (primelist[10000])
		break
