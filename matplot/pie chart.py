# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:28:14 2019

@author: prateek jain
"""

import matplotlib.pyplot as plt
import numpy as np


slices=[1,2,3,4,5,6,7,8]


act=['x','y','z','a','b','c','d','e']

plt.pie(slices,labels=act,explode=[0,0,0,0,0,0,0,0.1],radius=1,startangle=0,pctdistance=0.6,shadow=1,labeldistance=1.2,center=(2,2),autopct='%0.001f%%')
plt.legend()
plt.show()
