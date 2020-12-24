# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:08:09 2020

@author: kaysm
"""

import numpy as np

Input = list(map(int,list(open("day 23. input.txt", "r").read())))
#Input = list(map(int,list(open("sample.txt", "r").read())))

def crabCups(numberOfTurns):
    global arrangement
    global current
    turn = 1
    while True:
        indexOfCurrent = arrangement.index(current)
        
        pickedUp = []
        i = indexOfCurrent + 1
        while len(pickedUp) < 3:
            if i > len(arrangement)-1:
                i = 0
            pickedUp.append(arrangement[i])
            i = i + 1
            
        i = current-1
        while True:
            if i < min(arrangement):
                i = max(arrangement)
            if i not in pickedUp:
                destination = i
                break
            i = i -1
        
        for value in pickedUp:
           arrangement.remove(value)
        destinationIndex = arrangement.index(destination)
        arrangement = arrangement[0:destinationIndex+1] + pickedUp + arrangement[destinationIndex+1::]
        
        indexOfCurrent = arrangement.index(current)
        if indexOfCurrent == len(arrangement) -1:
            current = arrangement[0]
        else:
            current = arrangement[indexOfCurrent +1]
        
        if turn == numberOfTurns:
            break
            
        turn = turn + 1

# Deel 1 
arrangement = Input.copy()
current = arrangement[0]
crabCups(100)
arrangement = arrangement[arrangement.index(1)::] + arrangement[0:arrangement.index(1)]
result1 = "".join(list(map(str,arrangement[1::]))) 
print(result1)

## Deel 2 
#arrangement = Input.copy() + list(range(max(Input) + 1,1000001))
#current = arrangement[0]
#crabCups(1000000)
#arrangement = arrangement[arrangement.index(1)::] + arrangement[0:arrangement.index(1)]
#result2 = np.prod(arrangement[1:3])
#print(result2)
