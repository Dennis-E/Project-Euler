# Euler 23
# Sum of all numbers that are not the sum of two abundant numbers (under 28,123)

# Step 1: Find all abundant number under 28,123: Load it from file

# Step 2: Create all possible sums: Wrote it in a separate file

# Step 3: Exclude sums of two abundant_numbers from complete option space

list=[]
sums=[]

for i in range(1,28124):
	list.append(i)

with open(r"C:\Users\user\workspace\Euler\sums_of_abundant_numbers.txt") as F:
	for line in F:
		sums=line.split(",")

for i in sums:
	try:
		list.remove(int(i))
	except:
		pass

with open(r"C:\Users\user\workspace\Euler\numbers_not_sums_of_abundant_numbers.txt","w") as F:
	F.write(str(list))
			
print(sum(list))
