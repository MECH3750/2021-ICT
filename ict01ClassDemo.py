# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:36:37 2021

@author: uqcleon4
"""

import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x*x*x

# Create arrays for x and f(x)
h = 1
x = np.arange(-5,6,h,dtype=float)
f = f1(x)

# Calculate the forward difference
forwardD = np.zeros_like(f)
forwardD[:-1] = (f[1:] - f[:-1])/h

fig,ax =plt.subplots()
ax.plot(x, f,
        x[:-1], forwardD[:-1])
ax.grid()
plt.show()


 
    
    