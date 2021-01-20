# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:09:55 2019

@author: prateek jain
"""

import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'],index=['1','2'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

#df = df.append(df2,ignore_index=True)
df=pd.concat([df,df2],ignore_index=True)
print(df[2:4])

print('before deleting :\n',df)

del df['b']
print('\nafter deleting column:\n',df)
df=df.drop(2)
print('before deleting :\n',df)
