# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:07:22 2020

@author: kaysm
"""
import math

Input=open("day 13. input.txt", "r").read().split("\n")[:-1]
arrivalTime = int(Input[0])
possibleBusses = [int(bus) for bus in Input[1].split(",") if bus is not "x"]

# deel 1 
minimumWaitTime = math.inf
bestBus = None

for bus in possibleBusses:
    waittime = bus - (arrivalTime%bus)
    if waittime < minimumWaitTime:
        minimumWaitTime = waittime
        bestBus = bus
        result = bestBus * minimumWaitTime
        
print(result)

# deel 2 
possibleBusses = [[int(bus), Input[1].split(",").index(bus)] for bus in Input[1].split(",") if bus is not "x"]

time = possibleBusses[0][0]
addTime = possibleBusses[0][0]
addBusInTime = [possibleBusses[0][0]]

for i in range(1,len(possibleBusses)):
    bus, index = possibleBusses[i]
    while True:
        waittime = bus - (time%bus)
        if index > bus:
            index = index%bus
        if waittime == index:
            addBusInTime.append(bus)
            addTime = addTime * bus
            #print(time, waittime, index, addBusInTime)
            break

        time = time + addTime
print(time)
        