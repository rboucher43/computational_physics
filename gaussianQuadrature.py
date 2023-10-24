#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:10:33 2022

@author: reeseboucher

"""

from scipy.special import p_roots
from math import e
from numpy import arange
import matplotlib.pyplot as plt


# def f(x):
#     '''
#     Function that will be integrated

#     Parameters
#     ----------
#     x : float
#         Function input Value

#     Returns
#     -------
#     Float
#         Output Value

#     '''
#     return ((x**4) * e**x)/(((e**x) - 1)**2)


def gaussianQuadrature(a,b,N,f,funcN = -1):
    '''
    Uses the gaussian quadrature method to numerically evaluate integrals

    Parameters
    ----------
    a : float
        Lower integral bound
    b : float
        Upper integral bound
    N : Integer
        Number of sample points
    f : func
        Function that will be integrated
    funcN : float
        Input function value for fucntions with funcN dependence

    Returns
    -------
    I : Float
        Value of the integral

    '''
    x,w   = p_roots(N+1)   # Finds roots of legendre polynomial using scipy method

    if funcN ==  -1:
        I = ((b-a)/2) * sum(w * f(((b-a)/2) * x + ((b+a)/2)))
    else:
        I = ((b-a)/2) * sum(w * f(funcN,((b-a)/2) * x + ((b+a)/2)))
        
    return I



# gaussianQuadrature(0, 1, 50,f)


# def heatCapacity(T):
#     '''
#     Calculates heat capacity using Debye's Theory of Solids'

#     Parameters
#     ----------
#     T : float
#         Temperature of the system

#     Returns
#     -------
#     C_v: float
#         heat capacity of the solid with parameters defined in method

#     '''
#     volume         = 1          # meters**3
#     numberDensity  = 6.022e28   # meters**-3
#     debyeTemp      = 428        # kelvin
#     boltzmannConst = 1.38e-23   # Joules/Kelvin
    
#     C_v            = (9 * volume * numberDensity * boltzmannConst * (T/debyeTemp)**3) * gaussianQuadrature(0, (debyeTemp/T), 50, f)
    
#     return C_v

# heatCapacity(4)


# cvArr = []
# plotter    = arange(5,500)
# for i in range(5,500):    #Loop creates array full of heat capacities used to plot
#     cvArr.append(heatCapacity(i))
    
    
# plt.plot(plotter,cvArr)
# plt.xlabel('Temperature (K)')
# plt.ylabel('Heat Capacity (J/K)')
# plt.title('Heat Capity Curve (Dulong-Petit)')
# plt.savefig('heatCapacityCurve')
    