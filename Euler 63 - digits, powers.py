# -*- coding: utf-8 -*-
"""
Euler Problem 63

How many n-digit integers exists, that are an n-th power?

@author: Dennis Eggert
"""

count=0
i=0

while True:
    i+=1    
    for n in range(1,10):
        if len(str(n**i))==i:
            print(str(n)+"^"+str(i))
            count+=1
    if i==1000:
        print(count)
        break
            