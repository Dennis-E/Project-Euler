# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
counter=0

for i in range (123456788, 999999999):
    if "1" in str(i) and "2" in str(i) and"3" in str(i) and "4" in str(i) and "5" in str(i) and "6" in str(i) and "7" in str(i) and "8" in str(i) and "9" in str(i):
        counter+=1
for i in range(1000000000,9876543210):
    if "0" in str(i) and "1" in str(i) and "2" in str(i) and"3" in str(i) and "4" in str(i) and "5" in str(i) and "6" in str(i) and "7" in str(i) and "8" in str(i) and "9" in str(i):
        counter+=1
        if counter==1000000: 
            print("The "+str(counter)+"solution is: "+str(i))
