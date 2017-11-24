# Euler 50
# Number<1,000,000 that is made from longest sum of consecutive primes

def prime_list(number):
    if number==0 or number==1: return False
    if number==2: return ([2])
    result=[]
    for i in range(2,number+1):
        flag=True
        max_value=int(i**(1/2)+1)
        for factor in range(2,max_value):
            if i%factor==0:
                flag=False
                break
        if flag==True: result.append(i)
    return(result)

primes=prime_list(1000000)

maximum=0
i=0

for prime in primes:
    for j in range(i,len(primes)):
        candidate=sum(primes[i:j]) 
        if candidate<1000000 and candidate in primes and (j-i)>maximum:
            maximum=(j-i)
            result=candidate
    i+=1
print(result)