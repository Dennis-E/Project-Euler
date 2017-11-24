# Euler Problem 49
# 12 digit number as concatenated number from 3 4-digit numbers which have the same distance from each other, are prime and are permutations of each other

from itertools import permutations

def is_prime(number):
    max_value=int(number**(1/2)+1)
    if number==0 or number==1: return False
    if number==2: return True
    for i in range(2,max_value): #improved to only count until sqrt of number
        if number%i==0:
            return False
            break
    return True

candidates=[]

# All 4-digit primes
for i in range(1000,10000):
	if is_prime(i)==True: candidates.append(i)
print(len(candidates))

# Remove primes which have not 3 iterable primes
for candidate in candidates:
    count=0
    for element in permutations(str(candidate),4):
        if int(''.join(element)) in candidates:
            count+=1
    if count <3:
        candidates.remove(candidate)

# Remove primes which have not 3 primes in equal Distance
permutes2=[]
for candidate in candidates:
    candidates2=candidates[:]
    candidates2.remove(candidate)
    permutes=list(permutations(str(candidate),4))
    permutes2=[]
    for item in permutes:
        permutes2.append(int(''.join(item)))
    for candidate2 in candidates2:
        if candidate+2*(candidate2-candidate) in candidates and candidate2 in permutes2 and candidate+2*(candidate2-candidate) in permutes2 and candidate!=1487:
            print(str(candidate)+str(candidate2)+str(candidate+2*(candidate2-candidate)))