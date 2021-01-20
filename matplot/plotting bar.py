import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.bar(x,y,label='one',width=.3,bottom=6,align='edge',color='red',edgecolor='blue',linewidth=1,tick_label=[1,2,3,4,5])

plt.legend()
plt.show()

