#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 9 20:36:05 2022

@author: reeseboucher
"""

    
import numpy as np


def f(x):
    return ((np.sin(np.sqrt(100*x)))**2)


N = 2                  # number of slices
a = 0.0                # lower bound
b = 1.0                # upper bound 
w = (b-a)/N            # slice width
s = f(a)/2 + f(b)/2

for k in range(1, N):
    s += f(a+k*w)
    
I          = w * s
error      = abs((1/3)*I)  
I_minusone = 0 
loopCount  = 0      

print('Integral Estimate =',I)
print('Error             =',error)
print('Number of slices  =',N)
print('Loop Count        =',loopCount)
print('--------------------------------')


  
while(error > (10**-6)):
    loopCount += 1
    N = 2*N  
    w = w/2 
    I = I/2   

    for k in range(1, N, 2):  
        I += w * f(a + k*w)

    error      = abs((1/3)*(I - I_minusone))  
    I_minusone = I            
    
    
    print('Integral Estimate =',I)
    print('Error             =',error)
    print('Number of slices  = ', N)
    print('Loop Count        =', loopCount)
    print('--------------------------------')

