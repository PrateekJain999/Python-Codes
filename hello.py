# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:13:46 2019

@author: yogesh
"""

# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):
    __a=10
    def _init_(self):
        # call super() function
        super()._init_()
        
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin",self.__a)

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.__a=90
peggy.whoisThis()

peggy.swim()
peggy.run()