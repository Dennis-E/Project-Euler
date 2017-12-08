# -*- coding: utf-8 -*-
"""
Euler Problem 62

Find the smallest cube that has exactly five permutations that are also cube
"""
from itertools import permutations

cubes=[]
counter=0
i=45

while True:
    i+=1
    counter=0
    cubes.append(int(i**3))
    for permute in set(permutations(str(i**3))):
        if int(''.join(permute)) in cubes:
            counter+=1
    if counter==5:
        for permute in set(permutations(str(i**3))):
            if int(''.join(permute)) in cubes:
                print(''.join(permute))
                break
        break            