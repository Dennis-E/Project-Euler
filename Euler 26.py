# Euler 26
# Biggest recurring cycle

maximum=0
	
for i in range(2,1000):
	remainder=0.1
	list=[]
	length=0
	while True:
		remainder*=10
		if int(remainder)/i>1:
			if int(remainder) in list:
				length=len(list)-list.index(int(remainder))
				break
			else:
				list.append(int(remainder))
				remainder=int(remainder)%i
		elif int(remainder)==0:
			break
	
	if length>maximum:
		solution=i
		maximum=length

print(solution)
