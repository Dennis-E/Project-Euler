# Euler 22
# Opening a name list, sort alphabetical and assign a value to each name

names=[]
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
value=0

with open(r"C:\Users\user\workspace\Euler\Euler 22 p022_names.txt") as names_file:
	for line in names_file:
		currentline = line.split(",")
		names=currentline

sorted_names=sorted(names)
print(sorted_names[0])

for i in range(len(sorted_names)):
    name=sorted_names[i]
    for letter in name:
        for k in range(len(alphabet)):
            if letter==alphabet[k]:
                value+=k+1
    sorted_names[i]=(i+1)*value
    value=0

print(sorted_names[0])
print(sum(sorted_names))
