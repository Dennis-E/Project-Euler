# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
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
