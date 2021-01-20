import pandas as pd
import numpy as np

a=[-2,-1.7,0,7,np.nan]
b=[1,2,3,4]
c=[4,2,0,6,1]

Data=pd.Series(data=a, index=['a','b','c','d','e'], dtype=float, name=None, copy=False, fastpath=False)
Data1=pd.Series(data=b, index=['f','g','h','i'], dtype=float, name=None, copy=False, fastpath=False)
Data2=pd.Series(data=c, index=['a','b','c','d','e'], dtype=float, name=None, copy=False, fastpath=False)

print(Data)

print("Return a Series/DataFrame with absolute numeric value of each element :\n",Data.abs())

print("\nAddition of series and other, element-wise :\n",Data.add([1,2,3,4,5],fill_value=3,axis=0))

print("\nInvoke function on values of Series : \n",Data.apply(lambda Data : Data**2))

print("\ngives max value index : ",Data.idxmax())

print("\nConcatenate two or more Series. : \n",Data.append(Data1,ignore_index=True))

print("\nReturn boolean Series equivalent to left <= series <= right :\n",Data.between(-1,1,inclusive=True))

print("\nTrim values at input threshold :\n",Data.clip(-1,2,axis=0,inplace=False))

print("\nCombine the Series with a Series or scalar according to func :\n",Data.combine(Data2,max,fill_value=0))

print("\nCombine Series values, choosing the calling Series’s values first :\n",Data.combine_first(Data2))

print("\nReturn selected slices of an array along given axis as a Series :\n",Data2.compress(lambda Data2:Data2*2))

print("\nReturn number of non-NA/null observations in the Series :\n",Data.count())

print("\nCompute correlation with other Series, excluding missing values :\n",Data.corr(Data2,method='pearson',min_periods=3))

print("\nReturn cumulative maximum :\n",Data2.cummax())

print("\nCompute covariance with Series, excluding missing values :\n",Data.cov(Data2,min_periods=4))

print("\nReturn cumulative product :\n",Data.cumprod(axis=None,skipna=True))

print("\nDescribe series :\n",Data.describe())

print("\nFirst discrete difference of element :\n",Data.diff(periods=1))

print("\nFloating division od series :\n",Data.div(Data2,fill_value=1))

print("\nFloating division od series :\n",Data.divide(Data2,fill_value=1))

print("\nFloating division od series :\n",Data.div(Data2,fill_value=1))

d=Data.copy()
print("\ncopy series to other series :\n",d)

print("\nCompute the dot product between the Series :\n",Data.dot(Data2))

print("\nReturn Series with specified index labels removed :\n",Data.drop(labels=['a','b']))

print("\nReturn Series with duplicate values removed :\n",Data.drop_duplicates(keep=False))

print("\nReturn a new Series with missing values removed. :\n",Data.dropna(axis=0,inplace=False))

print("\nIndicate duplicate Series values :\n",Data.duplicated(keep=False))

print("\nIndicates Equal to of series and other :\n",Data.eq(Data2,fill_value=None,axis=0))

print("\nTest whether two objects contain the same elements :\n",Data.equals(Data2))

print("\nFill NA/NaN values using the specified method : \n",Data.fillna(5,axis=None,inplace=False,limit=None))

print("\nSubset rows or columns of dataframe according to labels in the specified index :\n",Data.filter(like='b',axis=0))

print("\nInteger division of series and other :\n",Data.floordiv(Data2))

print("\nGreater than or equal to of series and other :\n",Data.ge(Data2))

print("\nGet item from object for given key : \n",Data.get(key='a'))

print("\nindicates greater or not : \n",Data.gt(Data2))

print("\ngives top n values : \n",Data.head(2))

print("\nCheck whether values are contained in Series : \n",Data.isin([2,0]))

print("\nDetect missing values : \n",Data.isna())

print("\nAlias for index :\n",Data.keys())

print("\nReplace values where the condition is True :\n",Data.mask(Data>=0,10))

print("\nReturn the maximum of the values :",Data.max(axis=None,skipna=None))

print("\nmodulo of series and other series :\n",Data.mod(Data2))

print("\nReturn the largest n elements :\n",Data.nlargest(3))

print("\nReturn the largest n elements :\n",Data.nonzero())

print("\nDetect existing (non-missing) values :\n",Data.notna())

print("\nReturn number of unique elements in the object :\n",Data.nunique())

print("\nReturn item and drop from frame :\n",Data.pop('a'))

print("Exponential power of series and other :\n",Data.pow(2,fill_value=None,axis=0))

print("\nReturn the product of the values for the requested axis :",Data1.product(axis=None, skipna=None))

print("return Data+Data1 :\n",Data.radd(Data2))

print("\nassign rank acc to values :\n",Data.rank(axis=0,ascending=True))

print("\nRepeat elements of a Series :\n",Data.repeat(2))

print("\nReplace values given in to_replace with value :\n",Data.replace(0, value=5, inplace=False, limit=None))

print("\nRound each value in a Series to the given number of decimals :\n",Data.round(decimals=1))

print("\nReturn a random sample of items from an axis of object :\n",Data.sample(n=2, axis=None))

Data.set_axis([0,1,2,3], axis=0,inplace=True)
print("\nAssign desired index to given axis :\n",Data)

print("\nSort Series by index labels :\n",Data.sort_index(axis=0,ascending=False, inplace=False, kind='quicksort', na_position='last'))

print("\nSort Series by values :\n",Data.sort_values(axis=0,ascending=True, inplace=False, kind='quicksort', na_position='last'))

print("\nReturn the elements in the given positional indices along an axis :\n",Data.take([1,3],axis=0))

print("\nConvert Series to dict : 5",Data.to_dict())

print("\nTruncate a Series or DataFrame before and after some index value :\n",Data.truncate(before=2, after=3, axis=0))

print("\nReturn unique values of Series object : ",Data.unique())
Data.where(Data==0,'90')
print("\nModify Series in place using non-NA values from passed Series. Aligns on index : \n",Data)
