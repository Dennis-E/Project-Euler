# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:35:00 2017

Euler Problem 41
Find the largest pandigital (i.e. containing all n numbers from 1...n) prime number

@author: Dennis Eggert
"""
from itertools import permutations

print("hello world")

def is_prime(number): 
    max_value=int(number**(1/2)+1) 
    if number==0 or number==1: return False 
    if number==2: return True 
    for i in range(2,max_value): #improved to only count until sqrt of number 
        if number%i==0: 
            return False 
            break 
    return True 

i=0

while True:
    i+=1
    for item in (permutations(range(1,i+1))):
        number=""
        #Construct the number from the list of string elements        
        for element in item:
            number+=str(element)
        #Check if prime
        if is_prime(int(number)):
            print(number)
        if int(number)>987654321: break