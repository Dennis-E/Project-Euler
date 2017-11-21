# Euler 35
# Finding amount of primes were all rotations of digits are also primes under 1 mil

def is_prime(number):
    for i in range(2,int(number/(2-1))):
        if number%i==0:
            return False
            break
    return True

result=0

for i in range(2,1000001):
    all_prime=False
    prime_figures=[]
    if is_prime(i)==True:
        all_prime=True        
        for k in range(1,len(str(i))):
            if is_prime(int(str(i)[(-1)*(len(str(i))-k):]+str(i)[:(-1)*(len(str(i))-k)])):
                pass
            else:
                all_prime=False
                break

    if all_prime==True:
        print(i)
        result+=1
print(result)
