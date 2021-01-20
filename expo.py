import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('data.csv')
#data.hist(bins=[20,40,60,80],rwidth=0.2)
#print(data.head(2))
#print(data.corr())
print (data.to_string(index=False))
#print (data.describe())
#print (data.info())
#data=[15,10,13,18,16,27,34]
#plt.boxplot(data)
#plt.grid()
