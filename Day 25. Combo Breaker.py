# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:39:02 2021

@author: kaysm
"""

import math

Input = list(map(int,open("Day 25. input.txt", "r").read().split("\n")[:-1]))

cardPublicKey = Input[0]
doorPublicKey = Input[1]

def performHandshake(goal = math.inf, numberOfLoops = math.inf, subjectNumber = 7):
    loopSize = 0 
    key = 1
    while loopSize < numberOfLoops:
        key = key * subjectNumber 
        key = key % 20201227
        loopSize = loopSize + 1
        
        if numberOfLoops != math.inf:
            continue
        
        elif key == goal:
            break
 
    return [loopSize, key]

result = performHandshake(numberOfLoops = performHandshake(goal = cardPublicKey)[0], subjectNumber = doorPublicKey)[1]
print(result)
