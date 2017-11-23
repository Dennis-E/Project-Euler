# Euler 48
# The last ten digits of a huge sum

digits=0

for i in range(1,1001):
	number=i**i
	interim=number+int(digits)
	digits=str(interim)[-11:]
print(digits)