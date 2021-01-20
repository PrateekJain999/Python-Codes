import pandas as pd
import numpy as np

data = {'a' : 0.0, 'b' : 1.0, 'c' : 2.0}
s = pd.Series(data,index=['b','c','d','a'])
print(s)
print()
print(s[0:3])
print()
print(s[['b','d']])
print()
print('Returns a list of the row axis labels: ',s.axes)
print()
print('Returns True if series is empty: ',s.empty)
print()
print('Returns the number of dimensions of the underlying data, by definition 1. :',s.ndim)
print()
print('Returns the number of elements in the underlying data: ',s.size)
print()
print('Returns the Series as ndarray: ',s.values)
