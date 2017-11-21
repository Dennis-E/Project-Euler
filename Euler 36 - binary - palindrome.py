# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:43:29 2017
Euler 36
sum of all numbers under 1,000,000 where the decimal and the according binary representation are bith palindromes (i.e. figures "1" and "-1" the same)
@author: Dennis Eggert
"""

sum=0

for i in range(1,1000001):
    decimal = str(i)
    
    #Check if decimal is a palindrome
    check=True
    for length in range(len(decimal)):
        if decimal[length]==decimal[(-1)*(length+1)]:
            pass
        else:
            check=False
            break
    
    #Now check, in case decimal is palindrome, if also binary is
    if check==True:
        doublecheck=True
        binary = str(bin(i))
        for length in range(len(binary)-2):
            if binary[length+2]==binary[(-1)*(length+1)]:
                pass
            else:
                doublecheck=False
                break

    if check==True and doublecheck==True:
        print(decimal+" + "+binary)
        sum+=int(decimal)

print(sum)