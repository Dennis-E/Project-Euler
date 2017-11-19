# Euler Problem 42
# Read words from a file. Give each word a value = sum of lettervalues as defined by their position in alphabet and check if this is a triangle number, i.e. n*(n+1)/2
# Return the number of "triangular words"

#Returns the list of the first n triangle numbers
def triangle_numbers_list(n):
    triangle_numbers=[]
    for i in range(1,n+1): triangle_numbers.append(int(i*(i+1)/2))
    return triangle_numbers

#words to table
with open(r"C:\Users\user\workspace\Euler\Euler 42 words.txt") as F:
    for line in F:
        words=line.split(",")

#list of values of words
sums=[]
for word in words:
    sums.append(sum(ord(char)-96 for char in word.lower()))

maximum=max(sums)
triangle_numbers=triangle_numbers_list(maximum)

count=0
for item in sums:
    if item in triangle_numbers: count+=1
    else: pass

print(count)