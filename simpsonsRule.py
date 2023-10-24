#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:49:49 2022

@author: reeseboucher
"""



def f(x):
    return x**4 - 2*x + 1


N = 1000
a = 0.0
b = 2.0
w = (b-a)/N
s = 0.5*f(a) + 0.5*f(b) 
for k in range(1,N):  #loop for trapezoidal rule from the github pdf
    s += f(a+k*w) 
    
# print((w*s-4.4)/4.4)


def simpson(a,b,N): 
    '''
    Uses Simpson's rule to numerically evaluate integral'

    Parameters
    ----------
    a : float
        Lower integral bound
    b : float
        Upper integral bound
    N : Integer
        Number of slices

    Returns
    -------
    I : Float
        Value of the integral
        
    '''
    I      = 0
    steps  = (b-a)/N
    startB = b
    startA = b - steps
    
    for i in range(N):
        
        I += ((startB-startA)/6) * (f(startA)+ 4 * f((startA+startB)/2) + f(startB))
        
        startB = startA
        startA += -steps       
        
    # print(I)
    return I

# print(simpson(0,2,10))
    
print(simpson(0,2,10))
fractionalError = (simpson(0,2,10) - 4.4)/4.4
print(fractionalError)
print(simpson(0,2,100))
fractionalError = (simpson(0,2,100) - 4.4)/4.4
print(fractionalError)
simpson(0,2,1000)
print(simpson(0,2,1000))
fractionalError = (simpson(0,2,1000) - 4.4)/4.4
print(fractionalError)






