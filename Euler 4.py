# -*- coding: utf-8 -*-
"""
Euler #4
Dennis Eggert
"""

a=9
b=9
c=9
palindrome=100000*a+10000*b+1000*c+100*c+10*b+a
next=True

while next==True:
#check if the palindrome has two integer multipliers
    for i in range(999,99,-1):
        if palindrome%i==0 and palindrome/i<1000:
            print("The solution is: "+str(palindrome)+"because it is a multiple of "+str(i)+" and "+str(palindrome/i))
            next=False

#Check the next smaller palindrome
    if c==0: 
        c=9 
        if b==0: 
            b=9
            a=a-1
        else:
            b=b-1
    else:
        c=c-1 
    
    palindrome=100000*a+10000*b+1000*c+100*c+10*b+a
    if palindrome<=0: break
