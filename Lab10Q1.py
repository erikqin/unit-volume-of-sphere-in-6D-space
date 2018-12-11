#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 23:29:48 2017

@author: Xianan
"""

from numpy import random
from pylab import xlabel, ylabel,plot
N = 100
V = []
x = []
for k in range(100,1000,100):
    m = 0
    I = 0
    x.append(N)
    while (m<=N):
        x1 = random.random()
        x2 = random.random()
        x3 = random.random()
        x4 = random.random()
        x5 = random.random()
        x6 = random.random()
        I += 1
        if (x1**2+x2**2+x3**2+x4**2+x5**2+x6**2)<=1:
            m+=1
    V.append(2**6*m/I)
    N = 10*k
print(x)
plot(x,V)
xlabel('Monte-Carlo points')
ylabel('Volume of unit sphere in six-dimensions')

        