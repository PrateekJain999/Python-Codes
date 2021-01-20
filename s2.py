# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:56:44 2019

@author: yogesh
"""

import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve multiple elements
print (s[['a','c','d']])