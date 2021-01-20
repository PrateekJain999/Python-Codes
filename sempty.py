# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:16:41 2019

@author: yogesh
"""

import pandas as p
data={'Name':['yogesh','rajesh','priya'],'Section':['A','B','C']}
d=p.DataFrame(data,index=['Row1','Row2','Row3'])
print(d)