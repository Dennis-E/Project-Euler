# -*- coding: utf-8 -*-
"""
Euler 56
How many fractions have a numerator with more digits than denominator in the first
1,000 expansions for sqrt(1/2), i.e. always extending the latest denominator by +1/2

@author: Dennis Eggert
"""
counter=0
numerator=3
denominator=2

for i in range(1000):
    numerator2=2*denominator+numerator
    denominator2=numerator+denominator
    if len(str(numerator2))>len(str(denominator2)):
        counter+=1
    numerator=numerator2
    denominator=denominator2

print(counter)

"""
# Earlier try to construct the fraction through a string
# Runs into memory issues in eval

from fractions import Fraction

counter=0
expression="1+Fraction(1,2)"

for i in range(1000):
    print(i)
    brackets=0
    interim=list(expression)    
    #delete closing ")" terms
    for count in range(1,len(expression)):
        if expression[-count]==")": 
            del interim[-1]
        else:
            break
    expression=''.join(interim)
    # append "+1/2" in each cycle    
    expression+="+Fraction(1,2"
    #close all brackets    
    for count in range(len(expression)):
        if expression[count]=="(":brackets+=1
    for bracket in range(brackets):
        expression+=")"
    numerator=eval(expression).numerator
    denominator=eval(expression).denominator
    if len(str(numerator))>len(str(denominator)):
        counter+=1

print(counter)
"""