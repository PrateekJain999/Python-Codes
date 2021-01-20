# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:52:49 2019

@author: prateek jain

>


"""

class ABC:
    name='pk'
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def Print(self):
        print(self.first," ",self.last," ",self.name)

A1=ABC('Prateek','Jain')
A2=ABC('Prashuk','Jain')

print(ABC.__dict__)
print(A2.__dict__)
A2.Print()
