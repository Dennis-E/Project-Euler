# -*- coding: utf-8 -*-
"""
Euler Problem 60
Find the sum of five primes of which all combinations of any 2 concatenated numbers are also prime

@author: Dennis Eggert
"""
from itertools import permutations

def prime_list(number):
    # Input: Integer number
    # Returns: List of integer primes <= input number
    if number==0 or number==1: return False
    if number==2: return ([2])
    result=[]
    for i in range(2,number+1):
        flag=True
        max_value=int(i**(1/2)+1)
        if i%2==0:
            flag=False
            if i==2: flag=True
        for factor in range(3,max_value,2): #Improved: Check only uneven numbers
           if i%factor==0:
               flag=False
               break
        if flag==True: result.append(i)
    return(result)

def is_prime(number): 
    max_value=int(number**(1/2)+1) 
    if number==0 or number==1: return False 
    if number==2: return True 
    for i in range(3,max_value,2):  #Improved to only check uneven numbers 
        if number%i==0: 
            return False 
    return True 

def check_permute_pairs_are_primes(list):
    #Input: list of numbers as strings
    #Output: Bool
    #from itertools import permutations needed
    permutes=permutations(list,2)
    for permute in permutes:            
        if not is_prime(int(''.join(permute))):
            return False
    return True

primes=prime_list(10000)
to_check=["",""]
length=1
result=0

while True:   
    for figure1 in primes:
        to_check[0]=str(figure1)
        for figure2 in primes:
            if figure2>figure1:
                to_check=[str(figure1),str(figure2)]
                if check_permute_pairs_are_primes(to_check):
                    for figure3 in primes:
                        if figure3>figure2:                        
                            to_check=[str(figure1),str(figure2),str(figure3)]                            
                            if check_permute_pairs_are_primes(to_check):
                                for figure4 in primes:
                                    if figure4>figure3:                                    
                                        to_check=[str(figure1),str(figure2),str(figure3),str(figure4)]
                                        if check_permute_pairs_are_primes(to_check):
                                            for figure5 in primes:
                                                if figure5>figure4: 
                                                    to_check=[str(figure1),str(figure2),str(figure3),str(figure4),str(figure5)]                                           
                                                    if check_permute_pairs_are_primes(to_check):                                                    
                                                        print(to_check)                                                        
                                                        for element in to_check:
                                                            result+=int(element)
                                                        print(result)
                                                        result=0