# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 10:32:02 2019

@author: yogesh
"""

def sum():
    a=20
    b=30
    c=a+b
    print("Sum=",c)
sum()
def sum(a,b):
    c=a+b
    print("Sum=",c)
sum(10,30)
def sum(a,b):
    c=a+b
    return c
print("sum",sum(1,3))
