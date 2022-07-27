# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:36:37 2021
Edited on Wed Jul 27 13:12:00 2021

@author: uqcleon4
"""

import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x*x*x

def f1Prime(x):
    return 3*x*x

# Create arrays for x and f(x)
h = 0.5
x = np.arange(-5,6,h,dtype=float)
f = f1(x)

# Calculate the forward, backward, and central difference
forwardD = np.zeros_like(f)
forwardD[:-1] = (f[1:] - f[:-1])/h

backwardD = np.zeros_like(f)
backwardD[1:] = (f[1:]-f[:-1])/h

centralD = np.zeros_like(f)
centralD[1:-1] = (f[2:]-f[:-2])/(2*h)

# Calculate the error associated with each difference approach
fd = f1Prime(x)
errors = np.zeros((3,x.size))
errors[0,:-1] = fd[:-1] - forwardD[:-1]
errors[1,1:] = fd[1:] - backwardD[1:]
errors[2,1:-1] = fd[1:-1] - centralD[1:-1]

fig,ax =plt.subplots()
ax.plot(x, f,
        x[:-1], forwardD[:-1], '-.',
        x[1:], backwardD[1:], ':',
        x[1:-1], centralD[1:-1], '--')
ax.grid()
ax.legend(["f", "forwardD", "backwardD", "centralD"])

fig2,ax2 = plt.subplots()
ax2.plot(x[:-1], errors[0,:-1], '-.',
        x[1:], errors[1,1:], ':',
        x[1:-1], errors[2,1:-1], '--')
ax2.grid()
ax2.legend(["forwardD", "backwardD", "centralD"])

plt.show()


 
    
    
