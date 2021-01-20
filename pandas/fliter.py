# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:03:56 2019

@author: prateek jain
"""

import pandas as pd

#==========================================

#df=pd.read_csv('CSV.csv',parse_dates=['Date'])
#
#print(df.info())
#
##df['Volume'].astype('float')
#print(df.info())

#===========================================

df=pd.read_csv('iris.csv')

#print(df['SepalLengthCm']>5)

#print(df[df['SepalLengthCm']>5])
#
#print(df[df['Species'] == 'Iris-setosa'])

#print(df[(df['Species']=='Iris-versicolor') & (df['PetalLengthCm']>4.5)])

#========================= #isin method return using Or condition ==================================

#print(df[df['Species'].isin(['Iris-versicolor','Iris-virginica'])])  

#==================== isnull() method ==========================

#print(df['Species'].isnull())
#
#print(df[df['Species'].isnull()])

#==================== notnull() method ==========================

#print(df['Species'].notnull())
#
#print(df[df['Species'].notnull()])

#==================== between() method ==========================

#print(df[df['PetalLengthCm'].between(3,5,inclusive=True)])

#==================== duplicated() method ==========================

#df.sort_values('Species',inplace=True)
#print(~df['Species'].duplicated())
#print(df[df['Species'].duplicated()])                 #consider first name same nt duplicated

#==================== sort_index() method ==========================
#df.sort_index(inplace=True)
#print(df)

#==================== drop_duplicated() method ==========================

#print(df.drop_duplicates(subset=['Species','PetalLengthCm'],keep='first'))

#==================== set_index() method ==========================

#df.set_index('Id',inplace=True)
#print(df)

#df.reset_index(inplace=True)
#print(df)

#============================== loc ,iloc method ==============================

#print(df.iloc[5,1:3]) #index based 
#print(df.loc[5,'Id':'SepalWidthCm']) #label based
#print(df.loc[5,'Id':'SepalWidthCm']) #label,index based both works

#============================== query method ==============================

print(df.query("SepalLengthCm > 5 and 5<Id<50"))