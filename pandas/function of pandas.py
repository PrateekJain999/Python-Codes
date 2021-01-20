import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
   'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print ("Our dataframe is:")
print(df)

print(df.mean())
print()
print(df.corr())
print()
print(df.count())
print()
print(df.max())
print()
print(df.min())
print()
print(df.median())
print()
print(df.std())
