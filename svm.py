import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn import svm
from sklearn.model_selection import train_test_split  
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix
bankdata = pd.read_csv("bill_authentication.csv")  
bankdata.head()  
X = bankdata.drop('Class', axis=1)  
y = bankdata['Class'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
model = svm.SVC(kernel='linear')  
model.fit(X_train, y_train)   
y_pred = model.predict(X_test) 
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))  
print(y_pred)
print(classification_report(y_test,y_pred))
