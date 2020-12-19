# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:40:45 2020

@author: kaysm
"""

Input=open("day 18. input.txt", "r").read().split("\n")[:-1]
Tokenizer = [line.replace("(", "( ").replace(")", " )") for line in Input]
Tokenizer = [line.split(" ") for line in Tokenizer]

highPrecedence = ["("]
operators = ["+", "*"]

operatorPrecedence = {"+": 1, 
                      "*": 0}

def ShuntingYard(opdracht):
    resultList = []
    operatorList = []
    for token in opdracht:
        if token.isnumeric():
            resultList.append(token)
        elif token in operators:
            while len(operatorList) > 0 and operatorList[-1] is not "(" and operatorPrecedence[operatorList[-1]] >= operatorPrecedence[token]:
                resultList.append(operatorList.pop())
            operatorList.append(token)
        elif token == "(":
            operatorList.append(token)
        elif token == ")":
            while len(operatorList) > 0 and operatorList[-1] not in highPrecedence:
                resultList.append(operatorList.pop())
            if len(operatorList) > 0:
                operatorList.pop()
    while len(operatorList) > 0:
        resultList.append(operatorList.pop())

    return list(resultList)

def RPN(opdracht):
    resultList =[]
    for token in opdracht:
        if token.isnumeric():
            resultList.append(int(token))
        elif token in operators:
            number1 = resultList.pop()
            number2 = resultList.pop()
            result = performOperation(token, number1, number2)
            resultList.append(result)
    return int(resultList[0])

def performOperation(operator, number1, number2):
    if operator == "*":
        return number1 * number2
    if operator == "+":
        return number1 + number2
    
result1 = 0
for opdracht in Tokenizer:
    result1 = result1 + RPN(ShuntingYard(opdracht))

print(result1)

