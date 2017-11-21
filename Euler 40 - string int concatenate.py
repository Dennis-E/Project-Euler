# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:29:50 2017
Euler Problem 40
Concatenate behind "0," all ints and get the result of a certain multiplication 
@author: Dennis Eggert
"""
number="0,"

for i in range(1,1000001):
    number+=str(i)

print(int(number[0+2])*int(number[9+2])*int(number[99+2])*int(number[999+2])*int(number[9999+2])*int(number[99999+2])*int(number[999999+2]))