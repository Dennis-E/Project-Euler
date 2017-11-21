# Euler problem #43
# Return the sum of all pandigital (consists of figures 0-9) numbers for which sub-strings are divisible in a given way

from itertools import permutations

result=0
candidates=list(permutations('0123456789',10))

for candidate in candidates:
    # Making a string out of 3 list entries
    item=''.join(candidate)
    # And delete candidates with 0 in beginning
    if item[0]!="0": 
        if int(item[1:4])%2==0:
            if int(item[2:5])%3==0:
                if int(item[3:6])%5==0:
                    if int(item[4:7])%7==0:
                        if int(item[5:8])%11==0:
                            if int(item[6:9])%13==0:
                                if int(item[7:10])%17==0:
                                    result+=int(item)
                                    
print(result)