import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\yogesh\Downloads\fwdpythonml\Salary_Data.csv', encoding='latin-1')

print(df.head(n=60))
print(df.info())
print(df.describe())
print(df.columns)

X=df['YearsExperience']
y=df['Salary']
print(df.corr())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=0) # training methord


from sklearn.linear_model import LinearRegression
lm =LinearRegression() # import the LR
lm.fit(X_train,y_train)
prediction=lm.predict(X_test)
prediction1=lm.predict([[5]])
print("I AM PREDICTED",prediction1)

