# Euler 32
# Finding the sum of products whose multiplicand/multiplier/product identity 
# can be written as a 1 through 9 pandigital

set1=set()
set2=set()
set3=set()
set4=set()
set5=set()
set6=set()
result=set()

count=0
k=0

# Case 1: one-digit * 4 digit = 4 digits
for multiplicant in range(1,9):
    set1=set(range(1,10))
    set1.remove(multiplicant)
    for multiplier1 in set1:
        set2=set1.copy()
        set2.remove(multiplier1)
        for multiplier2 in set2:
            set3=set2.copy()
            set3.remove(multiplier2)
            for multiplier3 in set3:
                set4=set3.copy()
                set4.remove(multiplier3)
                for multiplier4 in set4:
                    set5=set4.copy()
                    set5.remove(multiplier4)
                    product=multiplicant*int(str(multiplier1)+str(multiplier2)+str(multiplier3)+str(multiplier4))
                    set6=set5.copy()
                    if len(str(product))==4:
                        for i in range(0,4):
                            try:
                                set6.remove(int(str(product)[i]))
                            except:
                                pass
                        if len(set6)==0:
                            result.add(product)
                            print(str(multiplicant)+"*"+str(multiplier1)+str(multiplier2)+str(multiplier3)+str(multiplier4)+"="+str(product))

# Case 2: two-digit * 3-digit = 4-digits
for multiplicant in range(1,10):
    set1=set(range(1,10))
    set1.remove(multiplicant)
    for multiplicant2 in set1:
        set2=set1.copy()
        set2.remove(multiplicant2)
        for multiplier1 in set2:
            set3=set2.copy()
            set3.remove(multiplier1)
            for multiplier2 in set3:
                set4=set3.copy()
                set4.remove(multiplier2)
                for multiplier3 in set4:
                    set5=set4.copy()
                    set5.remove(multiplier3)
                    product=int(str(multiplicant)+str(multiplicant2))*int(str(multiplier1)+str(multiplier2)+str(multiplier3))
                    set6=set5.copy()
                    if len(str(product))==4:
                        for i in range(0,4):
                            try:
                                set6.remove(int(str(product)[i]))
                            except:
                                pass
                        if len(set6)==0:
                            result.add(product)
                            print(str(multiplicant)+str(multiplicant2)+"*"+str(multiplier1)+str(multiplier2)+str(multiplier3)+"="+str(product))
                
print(sum(result))
