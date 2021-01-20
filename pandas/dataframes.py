# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:19:19 2019

@author: prateek jain
"""
import pandas as pd

Data={'day':pd.Series([1,2,3,4,5],index=['a', 'b', 'c','d','e']),
      'visitor':pd.Series([43,44,5,6,4],index=['a', 'b', 'c','d','e']),
      'rate':pd.Series([9,8,7,5,4],index=['a', 'b', 'c','d','e'])}

df=pd.DataFrame(Data)
print(df)
print()
print(df.tail())
print()
print(df.head())
print()
print(df.tail(2))
print()
print(df.loc['c'])
print()
print(df.iloc[2])
print()
#df=df.set_index('day') #temporary
df.set_index('day',inplace=True) #permanent
print(df)
