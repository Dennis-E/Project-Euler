#Euler 19
#Calculating the number of Sundays that fell on 1st of each month in the 20th century
#1.January 1901 a Tuesday according to google

residue=2
count=0
long=[1,3,5,7,8,10,12]	#months with 31 days
short=[4,6,9,11]		#months with 30 days

for year in range(1901,2001):
	for month in range(1,13):
		if month in long:
			days=31
		elif month in short:
			days=30
		elif month==2:
			if year%4==0:
				if year%100==0:
					if year%400==0:
						days=29
					else:
						days=28
				else:
					days=29
			else:
				days=28
		
		residue+=days%7
		if residue%7==0:
			count+=1				

print(count)
