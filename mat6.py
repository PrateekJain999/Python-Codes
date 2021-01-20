import matplotlib.pyplot as plt
exp_values=[1400,300,200,410,250]
exp_name=['House rent','Food','Phone Bill','Car','Other']
plt.pie(exp_values,labels=exp_name,radius=2,autopct='%0.2f%%',
        explode=[0,0.1,0,0.1,0],startangle=180)
plt.savefig('plt.png',bbox_inches='tight',pad_inches=2)