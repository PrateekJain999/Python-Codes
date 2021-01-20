# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:55:39 2019

@author: yogesh
"""
def numbers_to_strings(argument): 
    switch = {             
    1:"Sunday",
    2:"Monday",
	3:"Tuesday",
    4:"Wednesday",
    5:"Thursday",
    6:"Friday",
    7:"Satuarday",
    }
    return switch.get(argument, "nothing")
d=int(input("Enter the value of day"))
print(numbers_to_strings(d))
    