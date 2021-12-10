'''
CS 101 Lab
Program 13
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
Program must have functions for finding the total, average, or median or a list.
Program must be able to be tested on by another program via Unit Testing and pass.

ERROR HANDLING:
ZeroDivisionError when average function given list with 0 elements,
fixed by adding a check to the average function for if values list is empty.
'''

#ALGORITHM

import math

def total(values):
    total = 0
    for num in values:
        total+=num
    return float(total)

def average(values):
    if len(values) == 0:
        return math.nan
    total = 0
    for num in values:
        total+=num
    return float(total / len(values))

def median(values):
    if len(values) == 0:
        raise ValueError
    values.sort()
    center = len(values) / 2
    if center // 1 == center: #even number of elements in list
        return (values[int(center - 0.5)] + values[int(center + 0.5)]) / 2
    else: #odd number of elements in list
        return values[int(center)]
