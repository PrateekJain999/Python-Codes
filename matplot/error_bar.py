import matplotlib.pyplot as py

x=[1,2,3,4]
y=[2,2,3,1]
py.errorbar(x, y, yerr=.5,marker='s', xerr=1, ecolor='r', elinewidth=1,
            capsize=2, lolims=1, uplims=1,
            xlolims=1, xuplims=1, errorevery=1, capthick=3)
py.show()
