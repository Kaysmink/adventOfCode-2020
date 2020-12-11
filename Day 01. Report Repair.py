# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:33:22 2020

@author: kaysm
"""

import itertools as it
import numpy as np

Input=open("day 1. input.txt", "r").read().split("\n")
Input=list(map(int, Input))

# deel 1 
for value in Input:
    if 2020 - value in Input:
        print(value * (2020-value))
        break
    
# deel 2
for combination in it.combinations(Input, 3):
    if sum(combination) == 2020:
        print(np.product(combination))