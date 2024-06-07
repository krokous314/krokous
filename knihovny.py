# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 22:40:40 2022

@author: Lenovo
"""

import math
y = math.sin(x)

import numpy as np
data = np.arange(100)

from matplotlib.pyplot import plot
plot(data)

from numpy.ma import masked_array as ma
data = ma(data, mask=True)
#Existuje i zkratka, ale tu radši nepoužíváme, neb to neprospívá čitelnosti kódu.

from numpy import *
data = arange(100)

[2]