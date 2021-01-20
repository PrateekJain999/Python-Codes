import pandas as pd
import numpy as np

#==============================================================

"""d=pd.read_csv("ABCD.csv")

Data=pd.DataFrame(d)

print("csv file DataFrame :\n",Data)"""

#==============================================================

"""d = {'col1': [1, 2], 'col2': [3, 4]}=
df = pd.DataFrame("Dict DataFrame :\n",d)

print(df)"""

#===============================================================

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                    columns=['a', 'b', 'c'],index=['a', 'b', 'c'],dtype=float)
print("array DataFrame :\n",df2)
