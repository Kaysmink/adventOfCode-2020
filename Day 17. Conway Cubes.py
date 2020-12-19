# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:29:42 2020

@author: kaysm
"""

from collections import defaultdict
import itertools as it

# inlezen en klaarmaken data
Input=open("Day 17. input.txt", "r").read().split("\n")[:-1]

dimensions = defaultdict(list)
dimensions[0] = Input.copy()

def extendMatrix(oldDimensions):
    newDimensions = defaultdict(list)
    for key, value in oldDimensions.items():
        matrix = []
        for row in value:
            row = "." + row + "."
            matrix.append(row)
        matrix = ["."*len(matrix[0])] + matrix
        matrix.append("."*len(matrix[0]))
        newDimensions[key] = matrix
    return newDimensions
    
def calculateNewStateOfIndex(z,y,x,state):
    neighbors = []
    for combination in it.product([z-1,z,z+1], [y-1,y,y+1], [x-1,x,x+1]):
        neighbors.append(list(combination))
    neighbors = [[z,y,x] for z,y,x in neighbors if z in dimensions.keys() and y >= 0 and x >= 0 and x < maxX and y < maxY]
    neighbors.remove([z,y,x])
    #print(z,y,x, neighbors)
    counterActiveNeighbor = 0
    for z,y,x in neighbors:
        if dimensions[z][y][x] == "#":
            counterActiveNeighbor = counterActiveNeighbor + 1
    
    if state == "active":
        if counterActiveNeighbor in [2,3]:
            return "#"
        else:
            return "."
    if state == "inactive":
        if counterActiveNeighbor == 3:
            return "#"
        else: 
            return "."
    
def addNewDimension(iteration):
    newDimensions = [-iteration, iteration]
    
    for dimension in newDimensions:
        newMatrix = ["."*maxX] * maxY
        dimensions[dimension] = newMatrix

def calculateNewState(dimensions):
    newDimensions = defaultdict()
    
    for z in dimensions.keys():
        newMatrix = []
        for y in range(0,maxY):
            newRow = ""
            for x in range(0, maxX):
                if dimensions[z][y][x] == ".":
                    newRow = newRow + calculateNewStateOfIndex(z,y,x, "inactive")
                if dimensions[z][y][x] == "#":
                    newRow = newRow + calculateNewStateOfIndex(z,y,x, "active")
            newMatrix.append(newRow)
        newDimensions[z] = newMatrix              
    return newDimensions
                
def countActive(dimenions):
    counter = 0
    for z in dimensions.keys():
        for y in range(0,maxY):
            for x in range(0,maxX):
                if dimensions[z][y][x] == "#":
                    counter = counter + 1
    return counter

def printDimension():
    print("\n\niteratie: ",iteration)
    for key,value in dimensions.items():
        print("---------------------------------------")
        print("dimensie: ",key)
        for row in value:
            print(row)
    
iteration = 1

while iteration <= 6:
    dimensions = extendMatrix(dimensions)
    maxX = len(dimensions[0][0])
    maxY = len(dimensions[0])
    addNewDimension(iteration)
    dimensions = calculateNewState(dimensions)
    iteration = iteration + 1
    
print(countActive(dimensions))
