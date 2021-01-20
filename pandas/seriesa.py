import pandas as pd
##
##nba=pd.read_csv("ABC.csv",squeeze=True)
##
##print(nba)
##

a=['a','b','c','d','e','f',' ']
b=('a','b','c','d')
c={1:'a',2:'b',3:'c',4:'d'}

Data=pd.Series(data=a, index=[1,2,3,4,5,6,7], dtype=str, name=None, copy=False, fastpath=False)
print(Data)

Data1=pd.Series(data=b, index=[1,2,3,4], dtype=str, name=None, copy=False, fastpath=False)
print(Data1)

Data2=pd.Series(data=c, dtype=str, name=None, copy=False, fastpath=False)
print(Data2)

print("\nselection by position : ",Data.iloc[2])

print("\nTranspose : \n",Data.T)

print("\narray : ",Data.array)

print("\nAccess a single value for a row/column label pair : ",Data.at[5])

print("\nAccess a single value for a row/column pair by integer position :",Data.iat[3])

print("\nPurely integer-location based indexing for selection by position :",Data.iloc[2])

print("\nThe index (axis labels) of the Series :",Data.index)

print("\nReturn boolean if values in the object are unique :",Data.is_unique)

print("\nNumber of dimensions of the underlying data :",Data.ndim)

print("\nReturn a tuple of the shape of the underlying data :",Data.shape)

print("\nReturn the number of elements in the underlying data :",Data.size)

print("\nReturn Series as ndarray or ndarray-like depending on the dtype :",Data.values)
Data.fillna(0,axis=0,inplace=True)
print(Data)

