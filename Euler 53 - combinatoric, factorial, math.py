# Euler 53
# How many figures exists, with more than 1,000,000 combinations of an original figure with up to 100 digits and all possible r-length tuples of it

count=0

from math import factorial

for n in range(1,101):
    for r in range(1,n+1):
        if factorial(n)/(factorial(r)*factorial(n-r))>1000000:
            count+=1
print(count)