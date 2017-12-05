# Euler 58
# At which side length does the ratio of primes to overall numbers on both diagonals falls below 10% when the respective matrix is filled counter-clockwise with increasing primes

def is_prime(number):
    max_value=int(number**(1/2)+1)
    if number==0 or number==1: return False
    if number==2: return True
    for i in range(3,max_value,2):  #Improved to only check uneven numbers
        if number%i==0:
            return False
    return True

size=1
number=1
numerator=0
denominator=1

while True:
    size+=2
    for i in range(4):
        number+=size-1
        if is_prime(number):
            numerator+=1
    denominator+=4
    if numerator/denominator<0.1:
        break

print(size)