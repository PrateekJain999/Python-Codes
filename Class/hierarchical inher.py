# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:52:49 2019

@author: prateek jain
"""

class ABC1:   
    def print1(self):
        print('hi')
    def print2(self):
        print('hi')

class ABC2(ABC1):
    def print3(self):
        print('hi')
    def print4(self):
        print('hi')
        
class ABC3(ABC1):
    def print5(self):
        print('hi')

class ABC4(ABC2,ABC3):
    def print6(self):
        print('hi')


A1=ABC1()
A2=ABC2()
A3=ABC3()
A4=ABC4()

A1.print1()

