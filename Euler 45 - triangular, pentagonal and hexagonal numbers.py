# Euler Problem 45
# Find the first number > 40755 that is triangular, pentagonal and hexagonal

i=0

def is_triangular(n):
    if ((2*n+1/4)**0.5-1/2)%1==0:
        return True
    return False

def is_pentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

while True:
    i+=1
    hexagonal=i*(2*i-1)
    if is_pentagonal(hexagonal)==True and is_triangular(hexagonal)==True and hexagonal>40755:
        print(hexagonal)
        break