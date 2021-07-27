# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:30:23 2021

@author: uqcleon4
"""

import numpy as np
import matplotlib.pyplot as plt

# Define functions and their derivatives
def f1(x):
    return x*x*x

def f2(x):
    return 3*x*x - 2*x

def f3(x):
    return np.sin(x)

def f1Prime(x):
    return 3*x*x

def f2Prime(x):
    return 6*x - 2

def f3Prime(x):
    return np.cos(x)

# Create arrays for x and f(x)
h = 0.1
x = np.arange(-5,6,h,dtype=float)
f = f3(x)

# Calculate the forward, backward and central differences
forwardD = np.empty_like(f)
forwardD[:-1] = (f[1:]-f[:-1])/h

backwardD = np.empty_like(f)
backwardD[1:] = (f[1:]-f[:-1])/h

centralD = np.empty_like(f)
centralD[1:-1] = (f[2:]-f[:-2])/(2*h)

# Calculate the error associated with each difference approach
fd = f3Prime(x)
errors = np.zeros((3,x.size))
errors[0,:-1] = (fd[:-1]-forwardD[:-1])
errors[1,1:] = (fd[1:]-backwardD[1:])
errors[2,1:-1] = (fd[1:-1]-centralD[1:-1])

# Plot the function and each derivative approximation
fig,ax = plt.subplots()
ax.plot(x, f,
        x[:-1], forwardD[:-1], '-.',
        x[1:], backwardD[1:], ':',
        x[1:-1], centralD[1:-1], '--')
ax.set(xlabel="x", ylabel="f(x) and f'(x)")
ax.legend(["f", "forwardD","backwardD", "centralD"])
ax.grid()

# Plot the error associated with each difference approach
fig2,ax2 = plt.subplots()
ax2.plot(x[:-1], errors[0,:-1], '-.',
         x[1:], errors[1,1:], ':',
         x[1:-1], errors[2,1:-1], '--')
ax2.set(xlabel="x", ylabel="Error in f'(x)")
ax2.legend(["forwardD","backwardD", "centralD"])
ax2.grid()

plt.show()
