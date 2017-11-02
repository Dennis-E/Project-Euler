# -*- coding: utf-8 -*-
"""
Spyder Editor
 
This is a temporary script file.
"""
i=0
number1=1
number2=2
number3=0
counter=2

while i==0:    
    number3=number1+number2
    if number3>4000000:
        i=1
        exit
    if number3%2==0:
        counter=counter+number3
    number1=number2
    number2=number3
        
print("The solution is "+str(counter))

"""if i%3==0 or i%5==0:
        counter=counter+i
        print(str(i)+" "+str(counter))"""