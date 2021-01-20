import matplotlib.pyplot as plt

blood_sugar_women=[113,85,90,150,149,88,93,115,135,80,77,82,129]
blood_sugar_men=[80,129,95,130,139,83,97,105,115,87,71,85,119]

plt.hist([blood_sugar_men,blood_sugar_women],bins=[80,100,125,150],rwidth=0.9,label=['Women','Men'])
plt.legend()