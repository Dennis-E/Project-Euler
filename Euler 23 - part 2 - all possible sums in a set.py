# Euler 23
# Part 2
# Create a file with all sums of all abundant numbers < 28123

with open(r"C:\Users\user\workspace\Euler\list_of_abundant_numbers.txt") as F:
	for line in F:
		numbers1=line.split(",")

with open(r"C:\Users\user\workspace\Euler\list_of_abundant_numbers.txt") as G:
	for line in G:
		numbers2=line.split(",")

sums=set()
		
with open(r"C:\Users\user\workspace\Euler\sums_of_abundant_numbers.txt","w") as H:
	for number1 in numbers1:
		for number2 in numbers2:
			if int(number2)>=int(number1) and int(number1)+int(number2)<=28123:
				sums.add(int(number1)+int(number2))
	for sum in sums:
		H.write(str(sum)+", ")
