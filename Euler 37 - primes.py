# Euler 37
# Sum of the 11 primes where it is possible to remove one figure after the other from left to right or vice versa and the resulting numbers are also all primes_cache

def is_prime(number):
    max_value=int(number**(1/2)+1)
    if number==0 or number==1: return False
    if number==2: return True
    for i in range(2,max_value): #improved to only count until sqrt of number
        if number%i==0:
            return False
            break
    return True

result=0
count=0
number=7

while True:
    number+=1
    candidate=True
    for i in range(len(str(number))):
        if candidate==True and is_prime(int(str(number)[:(len(str(number))-i)]))==True:
            pass
        else:
            candidate=False
            break
        if candidate==True and is_prime(int(str(number)[((-1)*len(str(number))+i):]))==True:
            pass
        else:
            candidate=False
            break
    if candidate==True:
        result+=number
        print(number)
        count+=1
        
    if count==11: break

print(result)