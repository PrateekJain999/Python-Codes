import matplotlib.pyplot as py

x1=[1,2,3,4,5,6]
x2=[7,2,3,4,5,6]
x3=[8,2,3,4,5,6]
x4=[9,2,3,4,5,6]
py.boxplot([x1,x2,x3,x4], notch=None, vert=1,positions=[1,2,3,5],widths=0.8,
           patch_artist=1 ,usermedians=[2,5,3,4], showmeans=1,meanline=1,
           showcaps=1,showbox=1, labels=['a','b','c','d'],manage_xticks=1)

py.title('BOXPLOT')

py.show()
