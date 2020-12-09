# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:36:19 2020

@author: kaysm
"""

from collections import defaultdict
Input=open("day 7. input.txt", "r").read().split("\n")[:-1]

bagDictionary = defaultdict(list) 
searching = "shiny gold"

for line in Input: 
    line = line.split("bags contain ")
    headBag = line[0].strip()
    content = [x.strip().replace(".", "") for x in line[1].strip().split(",")]
    for bag in content:
        bag = bag.split(" ", 1)
        bagDictionary[headBag].append(bag[1].replace(" bags", "").replace(" bag", "").strip())
    
allColours = list(bagDictionary.keys())

possible = [colour for colour in allColours if searching in bagDictionary[colour]]

while True:
    newPossible    = []
    for colours in possible:
        new = [colour for colour in allColours if colours in bagDictionary[colour] and colour not in possible]
        newPossible.extend(new)

    if len(newPossible) == 0:
        break
    
    possible.extend(newPossible)
    possible = list(set(possible))

print(len(possible))



    