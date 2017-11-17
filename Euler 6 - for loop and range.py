sum_of_squares=0
summe=0

for i in range(1,101):
	sum_of_squares += i**2
	summe += i
	
print(summe**2-sum_of_squares)
