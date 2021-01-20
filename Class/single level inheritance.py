# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:52:49 2019

@author: prateek jain
"""

class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  