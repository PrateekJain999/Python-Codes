import matplotlib.pyplot as plt
import pandas as pd
m=[[1,0,0,2],
   [0,1,0,0],
   [0,0,1,0],
   [0,0,0,1]]
plt.matshow(m)
df=pd.DataFrame(m)
print(df.corr('pearson'))