# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:14:47 2017

@author: a1302594
"""

def is_prime(n):
    divisors=[]
    if n<=0: return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

maximum=0

for a in range(-1000,1001):
    for b in range(-1000,1001):
        i=-1
        while True:
            i+=1
            if is_prime(i**2+a*i+b)==True:
                True
            else:
                break
        length=i
        if length>maximum: 
            maximum=length
            factor1, factor2 = a, b

print(factor1)            
print(factor2)
print(maximum)

print(factor1*factor2)