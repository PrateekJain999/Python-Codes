import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[6,7,8,9,10]

plt.plot(x,y,marker='s',alpha=0.7,drawstyle='default',
         fillstyle='bottom',markersize=10,label='one',
         linestyle='-.',color='b',linewidth=1,
         markeredgecolor='r',markerfacecolor='k')
plt.axis([0,6,5,11])
plt.xlabel('NO')
plt.ylabel('population')
plt.title('Graph')
plt.plot([2,4,5],[6,7,8],label='two')
plt.grid()
plt.legend()
plt.show()

#a=plt.plot(x,y)                    #above method or this both are same (line=6)
#plt.setp(a,marker='s',markersize=10,label='one',linestyle='-.',color='b',linewidth=1,markeredgecolor='r',markerfacecolor='k')

"""
plt.plot([1,2,3,4,5],[0,1,3,4,5],marker='*',linestyle='--')
plt.plot([1,6,9,2,3],[6,7,8,9,0],marker='s')
#plt.plot([1,2,3,4,5],[0,1,3,4,5],'ro')
#plt.plot([1,2,3,4,5],[0,1,3,4,5],linestyle=':')"""
