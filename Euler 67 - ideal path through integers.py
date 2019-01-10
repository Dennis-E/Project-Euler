# Euler 67
# Calculating the ideal path for max sum through number triangle

# Read the triangle of integers

file=open(r"C:\Users\A1302594\Desktop\Python\Euler\67/p067_triangle.txt")

triangle_text=file.read()

# Loop through the lines
# split the lines
# transform into number
# write it in a list of lists
i=0
triangle=[[]]
for lines in triangle:
    triangle.append([int(x) for x in triangle_text.splitlines()[i].split()])
    i+=1
    if i==100:break
triangle.pop(0)         # I don't know why but I had to add the empty list in the beginning otherwise he didnt append

values=[[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

n=100       # number of layers in the pyramid
sum=0

# Calculating the "Worth" of each knot in the tree 
# Starting from the lowest layer
# Step by step deciding for the more worthy knot in the layer below
# and adding the own "worth"
for layer in range(n-2,-1,-1):
    print(layer)
    for i in range(0,len(triangle[layer])):
        triangle[layer][i]+=max([triangle[layer+1][i],triangle[layer+1][i+1]])

print(triangle[0:4])
print(triangle[0][0])
print("The highest possible sum is: "+str(triangle[0][0]))

#7273 is the correct solution