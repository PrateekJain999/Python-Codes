import matplotlib.pyplot as plt


students=['Sunny','Abhishek','Rajesh','Raman']
getmarks=[800,600,750,650]
less=[200,400,250,350]
#index=[0,1,2,3]
plt.xlabel('Students')
#plt.xticks(index,year)
plt.title('Students Marks')
plt.ylabel('Marks out of 1000')
plt.bar(students,getmarks,color="red")
plt.bar(students,less)
