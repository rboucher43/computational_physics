#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 21:57:11 2022

@author: reeseboucher

Script uses adaptive simpson's method with accuracy 
threshold to numerically calculate integral

"""
import numpy as np


def f(x):
    return np.sin(np.sqrt(100*x))**2


N          = 1                # Number of slices
a          = 0                # upper bound
b          = 1                # lower bound
w          = (b-a)/N          # width        
s          = f(a)/3 + f(b/3)       
t          = (2/3) * f(a + w)              
I          = w * (s + 2*t)         
error      = abs((1/15)*(w*I))   

I_minusone = 0            
loopCount  = 0 
     
while(error > (10**-6)):
    loopCount += 1  
    N         = N*2  
    w         = (b-a)/N  
    s         += t  
    t         = 0  

    for k in range(1, N, 2):  
        t += (2/3)*f(a + k*w)

    I          = w*(s + 2*t)  
    error      = abs((1/15)*(I - I_minusone))  
    I_minusone = I          

    print('Integral Estimate =',I)
    print('Error             =',error)
    print('Number of slices  =',N)
    print('Loop Count        =',loopCount)
    print('--------------------------------')
