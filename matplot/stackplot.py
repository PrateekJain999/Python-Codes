# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:28:14 2019

@author: prateek jain
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:04:40 2019

@author: prateek jain
"""

import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3]
y=[4,5,6]
z=[7,8,9]
a=[1,2,3]

plt.grid()

plt.stackplot(a,x,y,z,colors=['k','m','yellow'])
plt.legend()