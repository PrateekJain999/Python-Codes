# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\yogesh\Desktop\tanu.txt')
print(df.head(2))
plt.plot(df['a'],df['b'])