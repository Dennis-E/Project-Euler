# Euler Problem 44
# Find the minimum difference between two figures that are both pentagonal as well as their sum and difference is pentagonal

i=0
pentagonals=set()

def is_pentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False
    
while True:
    i+=1
    pentagonal_number=int((i*(3*i-1))/2)
    pentagonals.add(pentagonal_number)
    for element in pentagonals:
        if is_pentagonal(pentagonal_number+element) and is_pentagonal(pentagonal_number-element):
            print(pentagonal_number-element)
            break