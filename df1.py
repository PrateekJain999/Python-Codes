# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:20:35 2019

@author: yogesh
"""

import pandas as pd
data={'Name':['yogesh','deepti','diksha','rajesh'],'section':['a','b','c','d']}
s=pd.DataFrame(data)
print(s['section'].describe())