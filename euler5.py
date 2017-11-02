# -*- coding: utf-8 -*-
"""
Spyder Editor
 
This is a temporary script file.
"""



"""Euler #4
a=9
b=9
c=9
palindrome=100000*a+10000*b+1000*c+100*c+10*b+a
next=True

while next==True:
#check if the palindrome has two integer multipliers
    for i in range(999,99,-1):
        if palindrome%i==0 and palindrome/i<1000:
            print("The solution is: "+str(palindrome)+"because it is a multiple of "+str(i)+" and "+str(palindrome/i))
            next=False

#Check the next smaller palindrome
    if c==0: 
        c=9 
        if b==0: 
            b=9
            a=a-1
        else:
            b=b-1
    else:
        c=c-1 
    
    palindrome=100000*a+10000*b+1000*c+100*c+10*b+a
    if palindrome<=0: break


---------------------------------------------------------------------------
Euler #3
i=0
factors=[]
next=True

target=600851475143

while next==True:
    i=i+1
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
    if prime==True and target%i==0:
        print(i)
        target=target/i
        factors.append(i)
    if target==0:
        next=False
 
print("The biggest factor is: "+max(factors))


---------------------------------------------------------------------------
Euler #2

i=0
number1=1
number2=2
number3=0
counter=2

while i==0:    
    number3=number1+number2
    if number3>4000000:
        i=1
        exit
    if number3%2==0:
        counter=counter+number3
    number1=number2
    number2=number3
        
print("The solution is "+str(counter))

---------------------------------------------------------------------------
Euler #1
    if i%3==0 or i%5==0:
        counter=counter+i
        print(str(i)+" "+str(counter))
"""