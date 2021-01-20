5# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:46:38 2019

@author: prateek jain
"""

import pandas as pd
import numpy as np

data = [['Alex',10],['Bob',12],['Clarke',13]] #lists

df = pd.DataFrame(data,index=['rank1','rank2','rank3'],columns=['Name','Age']
                  ,dtype=int)

print(df[['Name','Age']])
print()
print(df.Name)
print()
print('list conversion : ', df.Name.tolist())
print()
print('list conversion : ',np.array(df[['Name','Age']]))
