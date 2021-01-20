# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:04:40 2019

@author: prateek jain
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1,50)
y=np.random.randn(1,50)

plt.scatter(x, y, s=50, c=None, marker='o',alpha=0.7,
            linewidths=1,verts=None, edgecolors='r')
plt.show()
