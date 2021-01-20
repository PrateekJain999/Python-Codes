import pandas as pd
import numpy as np


df = pd.DataFrame(np.array([[1, None, 3], [-4, 3, 3], [-4,3,3]]),
                    columns=['a1', 'b1', 'c1'],index=['a2', 'b2', 'c2'],dtype=float)

df2 = pd.DataFrame(np.array([[1, 1, 1], [1,1,1], [1,1,1]]),
                    columns=['a1', 'b1', 'c1'],index=['d2', 'e2', 'f2'],dtype=float)


df3 = pd.DataFrame(np.array([[1, 1, 1], [2,2,2], [3,3,3]]),
                    columns=['a1', 'b1', 'c1'],index=['a2', 'b2', 'c2'],dtype=float)

print("array DataFrame :\n",df)

#print("\nReturn aDataFrame with absolute numeric value of each element :\n",df.abs())
#
#print("\nReturn aDataFrame with adding prefix on column :\n",df.add_prefix('item_'))
#
#print("\nReturn aDataFrame with absolute numeric value of each element :\n",df.add(2, axis=0, level=None, fill_value=None))
#
#print("\nReturn aDataFrame with adding suffix on column :\n",df.add_suffix('_ind'))
#
#print("\nAppend rows of other to the end of caller, returning a new object :\n",df.append(df2, ignore_index=True))
#
print("\nApply a function along an axis of the DataFrame :\n",df.apply(np.sum, axis=1))
#
print("\nassign new column to the DataFrame :\n",df.assign(d1=lambda x: x.a1 + x.b1 + x.c1))
#
print("\nTrim values at input threshold :\n",df.clip(lower=0, upper=5, axis=None, inplace=False))
#
#print("\nTrim values at input threshold :\n",df.combine_first(df3))
#
#df4=df.copy()
#print("\nMake a copy of this object’s indices and data \n:",df4)
#
#print("\nCompute pairwise correlation of columns, excluding NA/null values. :\n",df.corr(method='pearson', min_periods=1))
#
#print("\nCount non-NA cells for each column or row :\n",df.count(axis=0))
#
#
#print("\nCompute pairwise covariance of columns :\n",df.cov(min_periods=None))
#
#print("\nReturn cumulative maximum over a DataFrame \n",df.cummax(axis=None, skipna=True))
#
#print("\nReturn cumulative minimum over a DataFrame \n",df.cummin(axis=None, skipna=True))
#
#print("\nReturn cumulative product over a DataFrame \n",df.cumprod(axis=None, skipna=True))
#
#print("\nReturn cumulative sum over a DataFrame \n",df.cumsum(axis=None, skipna=True))
#
#print("\nGenerate descriptive statistics \n",df.describe(percentiles=None, include=None, exclude=None))
#
#print("\nFloating division of dataframe and other, element-wise \n",df.div(df3, axis='columns', level=None, fill_value=None))
#
#print("\nCompute the matrix mutiplication between the DataFrame and other \n",df.dot([1,2,3]))
#
print("\nDrop specified labels from rows or columns \n",df.drop(axis=0, index='a2', columns='a1', inplace=False))
#
#print("\nReturn DataFrame with duplicate rows removed \n",df.drop_duplicates(subset=None, keep='first', inplace=False))
#
#print("\nRemove missing values \n",df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False))
#
#print("\nReturn boolean Series denoting duplicate rows \n",df.duplicated(subset=None, keep='first'))
#
#print("\nEqual to of dataframe and other, element-wise \n",df.eq(3, axis='columns', level=None))
#
#print("\nTest whether two objects contain the same elements \n",df.equals(df3))
#
#print("\nEvaluate a string describing operations on DataFrame columns \n",df.eval('d1=a1+b1+c1', inplace=False))
#
#print("\nFill NA/NaN values using the specified method \n",df.fillna(value=4, axis=0,method=None , inplace=False, limit=2))
#
#print("\nSubset rows or columns of dataframe according to labels in the specified index \n",df.filter(items=['a1','c1'], like=None, regex=None, axis=None))
#
#print("\nInteger division of dataframe and other, element-wise \n",df.floordiv(df3, axis='columns', level=None, fill_value=None))
#
#print("\nGreater than or equal to of dataframe and other, element-wise \n",df.ge(df3, axis='columns', level=None))
#
#print("\nGet item from object for given key(DataFrame column)  \n",df.get('a1', default=None))
#
print("\nQuickly retrieve single value at passed column and index:  \n",df.get_value('a2', 'a1'))
#
#print("\nGreater than of dataframe and other, element-wise  \n",df.gt(df3, axis='columns', level=None))
#
#print("\nreturn first n rows  \n",df.head(2))
#
#print("\nReturn index of first occurrence of maximum over requested axis  \n",df.idxmax(axis=0, skipna=True))
#
#df.insert(3, 'd1', [1,2,3], allow_duplicates=False)
#print("\nInsert column into DataFrame at specified location \n",df)
#
#print("\n  \n",df.isin([1,2,3]))
#
print("\nchecks na vlaues  \n",df.isna())
#
#print("\nGet the ‘info axis : \n",df.keys())
#
print("\nreplace values when cond is true : \n",df.mask(df<1, other=2, inplace=False, axis=None, level=None))
#
#print("\nReturn the mean of the values for the requested axis : \n",df.mean(axis=None, skipna=None))
#
#print("\nReturn the median of the values for the requested axis : \n",df.median(axis=1, skipna=None))
#
#print("\nCount distinct observations over requested axis :\n",df.nunique(axis=1, dropna=True))
#
#print("\nReturn item and drop from frame :\n",df.pop('a1'))
#
#print("\nExponential power of dataframe and other, element-wise :\n",df.pow(2, axis='columns', level=None, fill_value=None))
#
#print("\nReturn the product of the values for the requested axis. :\n",df.prod(axis=None, skipna=None))
#
##print("\nReturn item and drop from frame :\n",df.pop('a1'))
#
#
#
#
#
#
#
#
#
