# -*- coding: utf-8 -*-
"""
Euler Problem 55
 
How many numbers under 10,000 are lychrel numbers, i.e. numbers that never become 
palidromes (numbers that are the same written from the front and from the back)
through a process of adding to the original number the "reversed" number.

Assumption: If within 50 iterations its a palindrome it is not.
"""

def reverse_number(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False

counter=0

for i in range(10,10000):
    previous_result=i
    flag=False    
    for iteration in range(51):    
        result=previous_result+reverse_number(previous_result)
        if is_palindrome(result):
            flag=True
            break
        else:
            previous_result=result
    if flag==False:
        counter+=1
        
print(counter)