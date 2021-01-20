# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:56:18 2019

@author: prateek jain
"""

import matplotlib.pyplot as plt

x2=[1,1,1,1,2,1,3,4,5,6]
y2=[1,2,3,3,3,3,4,4,5,6]
z2=[1,2,3,4,5,7,5,5,6,6]
plt.hist([x2,y2,z2],bottom=None,density=1, histtype='bar', align='mid', orientation='vertical',
         rwidth=.7, log=0, color=['r','k','y'], label=['x','y','z'])

plt.legend()
plt.show()
