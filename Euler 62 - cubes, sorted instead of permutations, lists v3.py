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
    if i%100==0:print(i)
    counter=0
    new_cube=i**3
    new_cube_string=sorted(str(new_cube))
    length=len(new_cube_string)
    cubes.append(new_cube)
    interim_cubes=cubes[:]
    #Delete cubes that are to short to be permutations
    for cube in cubes:
        if len(str(cube))<length:
            interim_cubes.remove(cube)
    cubes=interim_cubes[:]
    #Check if cubes of same length until now are permutations
    for cube in cubes:
        if sorted(str(cube))==new_cube_string:
            counter+=1
            if counter==5:
                #Return the first (i.e. the smallest) permutation                
                for cube in cubes:
                    if sorted(str(cube))==new_cube_string:
                        print(cube)
                        break
                break
    if counter==5:break
if counter==5:exit