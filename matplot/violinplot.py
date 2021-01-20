import matplotlib.pyplot as plt

x=[1,2,3,4,3,2,1]

plt.violinplot(x, positions=[2], vert=True, widths=0.5,
               showmeans=1, showextrema=True, showmedians=1, points=100)
plt.show()
