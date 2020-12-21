# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 12:17:31 2020

@author: kaysm
"""

from collections import defaultdict

Input=open("day 20. input.txt", "r").read().split("\n\n")[:-1]

tileDict = defaultdict()
for tile in Input:
    key, tile = tile.split("\n",1)
    key = int(key.replace("Tile ", "").replace(":", ""))
    tile = [list(line) for line in tile.split("\n")]
    tileDict[key] = tile

# Deel 1 
bordersDict = defaultdict()
for key, tile in tileDict.items():
    borders = defaultdict()
    top = tile[0]
    down = tile[-1]
    
    left = []
    right = []
    
    for y in range(0,len(tile)):
        left.append(tile[y][0])
        right.append(tile[y][-1])
    
    borders["top"] = top
    borders["down"] = down
    borders["left"] = left
    borders["right"] = right
    
    borders["reverse top"] = top[::-1]
    borders["reverse down"] = down[::-1]
    borders["reverse left"] = left[::-1]
    borders["reverse right"] = right[::-1]
    
    bordersDict[key] = borders

corners = []
for tile, value in bordersDict.items():
    numOfNeighbors = 0
    for tile2, value2 in bordersDict.items():
        if tile == tile2:
            continue
        for orientation, border in value.items():
            for orientation2, border2 in value2.items():
                if border == border2:
                    numOfNeighbors = numOfNeighbors + 1
    if numOfNeighbors == 4:
        corners.append(tile)

result1 = 1
for value in corners:
    result1 = result1 * value

print(result1)