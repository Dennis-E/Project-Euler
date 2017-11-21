# Euler Problem 39
# Maximum # of solutions for integer side length for right-angle triangles with perimeter <=1,000

maximum=0

for perimeter in range(1,1001):
    count=0
    for side1 in range(1,perimeter):
        if (2*(side1-perimeter))!=0:
            side2=(perimeter**2)/(2*(side1-perimeter))+perimeter
        else:
            side2=-1
        if side2%1==0 and side2>0:
            count+=1
    if count>maximum:maximum=perimeter
print(maximum)