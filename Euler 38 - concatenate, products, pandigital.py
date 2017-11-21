# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:12:11 2017
Euler problem 38
Searching the highest pandigital figure that is the concatenated products of an integer with range(1,n) with n>1

@author: Dennis Eggert
"""

def is_pandigital(n):    
    numbers="123456789"
    for char in numbers:
        if char not in str(n):
            return False
    return True

i=987654321
candidate=False

while True:
    if is_pandigital(i):
        if int(str(i)[-5:]) == 2*int(str(i)[:4]):
            candidate=True
        if int(str(i)[-3:]) == 2*int(str(i)[-6:-3]) == 3*int(str(i)[:2]):
            candidate=True
        if int(str(i)[-3:]) == 2*int(str(i)[-5:-3]) == 3*int(str(i)[-7:-5]) == 4*int(str(i)[-9:-7]):
            candidate=True
    if candidate==True:
        print(i)
        break
    i-=1