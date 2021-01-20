import pandas as pd
import numpy as np


df = pd.DataFrame(np.array([[1, -2, 3], [-4, 5, 6], [7, -8, 9]]),
                    columns=['a1', 'b1', 'c1'],index=['a2', 'b2', 'c2'],dtype=float)
print("array DataFrame :\n",df)

print("\nTranspose DataFrame :\n",df.T)

print("\nAccess a single value for a row/column label pair :\n",df.at['a2','b1'])

print("\nReturn a list representing the axes of the DataFrame :\n",df.axes)

print("\nIndicator whether DataFrame is empty :\n",df.empty)

print("\nThe column labels of the DataFrame :\n",df.columns)

print("\nReturn the dtypes in the DataFrame :\n",df.dtypes)

print("\nAccess a single value for a row/column pair by integer position :",df.iat[1,2])

print("\nPurely integer-location based indexing for selection by position :\n",df.iloc[0,1])

print("\nThe index (row labels) of the DataFrame :\n",df.index)

print("\nAccess a group of rows and columns by label(s) or a boolean array :\n",df.loc[['a2','b2']])

print("\nReturn an int representing the number of axes / array dimensions : ",df.ndim)

print("\nReturn a tuple representing the dimensionality of the DataFrame :\n",df.shape)

print("\nReturn an int representing the number of elements in this object :\n",df.size)

print("\nReturn a Numpy representation of the DataFrame :\n",df.values)
