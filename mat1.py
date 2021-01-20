# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:26:59 2019

@author: yogesh
"""

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[30,40,50,30,20]
plt.xlabel('marks')
plt.title('college management')
plt.ylabel('students marks')
plt.plot(x,y,'rD--')
#plt.plot(x,y,marker='+' ,color='red',linestyle='dotted',linewidth='10' )