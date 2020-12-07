# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:58:05 2020

@author: kaysm
"""

Input=open("day 6. input.txt", "r").read().split("\n\n")

# deel 1 
result1 = 0 

for line in Input:
    distinctCharacters = set(line.replace("\n", ""))
    result1 = result1 + len(distinctCharacters)
    
# deel 2 
result2 = 0 
for line in Input:    
    for group in line.split("\n\n"):
        person = group.split("\n")
        person = filter(None, person)
        yesList = []
        for answer in person:
            yesList.append(list(set(answer)))
        print(yesList)
        result2 = result2 + len(list(set(yesList[0]).intersection(*yesList)))