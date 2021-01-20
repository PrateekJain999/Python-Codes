# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:04:13 2019

@author: prateek jain
"""

import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
   'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print ("Our dataframe is:")
print(df)
print()

print('Transposes rows and columns. : \n',df.T)
print()

print('Returns a list with the row axis labels and column axis labels as the only members : ',df.axes)
print()

print('True if NDFrame is entirely empty : ',df.empty)
print()

print('Number of axes / array dimensions. : ',df.ndim)
print()

print('Returns a tuple representing the dimensionality of the DataFrame. : ',df.shape)
print()

print('Number of elements in the NDFrame : ',df.size)
print()

print('Numpy representation of NDFrame : \n',df.values)
print()

print('Returns the first n rows. : \n',df.head())
print()

print('Number of non-null observations. : \n',df.count())
print()

print('Sum of values. : \n',df.sum())
print()

print('Standard Deviation of the Values. : \n',df.std())
print()

print('Mean of Values. : \n',df.mean())
print()

print('mode of Values. : \n',df.mode())
print()

print('absolute value. : \n',df.abs())
print()

print('product of Values. : \n',df.prod())
print()

print('cumulative sum. : \n',df.cumsum())
print()

print('describe. : \n',df.describe())
print()

# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print(df)

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print(df)
