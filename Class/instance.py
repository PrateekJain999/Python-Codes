# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:52:49 2019

@author: prateek jain
"""

class ABC:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def print(self):
        print(self.first," ",self.last)

A1=ABC('Prateek','Jain')
A2=ABC('Prashuk','Jain')

print(A1.first ,end=' ')
print(A1.last)
print(A2.first ,end=' ')
print(A2.last)
A2.print()