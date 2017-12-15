# -*- coding: utf-8 -*-
"""
Euler Problem 64

Return # of integers <10000 whose sqrt, when depicted as an iterative fraction, has an odd period

@author: Dennis Eggert

Algoritms (copy with pride) from Wikipedia:
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
"""
result=0
a2=int
d2=int
m2=int

for i in range(1,10001):
    periods=[]
    counter=0
    flag=True
    a=()
    m1=0
    d1=1
    a1=int(i**(1/2))
    if a1**2==i:
        pass
    else:
        while flag==True:
            counter+=1
            m2=d1*a1-m1
            d2=int((i-(m2**2))/d1)
            a2=int((i**(1/2)+m2)/d2)
            if (a2,d2,m2) in periods:
                flag=False
            else:
                periods.append((a2,d2,m2))
            m1=m2
            d1=d2
            a1=a2
        if counter%2==0:
            result+=1
print(result)