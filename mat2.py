import matplotlib.pyplot as plt

days=[1,2,3,4,5,6,7]
maxtemp=[70,54,40,60,70,50,70]
mintemp=[30,20,31,18,16,21,19]
avgtemp=[34,23,37,29,28,25,20]
plt.xlabel('Days')
plt.title('Weather')
plt.ylabel('Temperature')
plt.plot(days,maxtemp,label="max",alpha=1,linewidth="6")
plt.plot(days,mintemp,label="min")
plt.plot(days,avgtemp,label="Avg",color='red')
plt.legend(loc="best",fontsize='small')
plt.grid()