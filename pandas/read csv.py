

import pandas as pd

"""

df=pd.read_csv('ABC.csv',names=['A','B','C','D','E','F'])
df.to_csv('ABCD.csv',header=0) #new file save
df2=pd.read_csv('ABC.csv',names=['A','B','C','D','E','F']) 
print(df2.head())

"""

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print()
print(df.loc['b']) #gives index loction
print(df.iloc[3]) #gives data of 3 row in diff columns
