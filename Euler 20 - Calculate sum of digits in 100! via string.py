# Euler20
# Calculating the sum of digits of 100!

number=1
Summe=0

for i in range(1,101):
	number*=i
	
for i in range(len(str(number))):
	Summe+=int(str(number)[i])
print(Summe)
